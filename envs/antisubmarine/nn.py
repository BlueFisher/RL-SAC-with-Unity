import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp

import algorithm.nn_models as m


class ModelTransition(m.ModelBaseTransition):
    def __init__(self, state_dim, action_dim, use_extra_data):
        super().__init__(state_dim, action_dim, use_extra_data)

        self.dense = tf.keras.Sequential([
            tf.keras.layers.Dense(128, activation=tf.nn.relu),
            tf.keras.layers.Dense(128, activation=tf.nn.relu),
            tf.keras.layers.Dense(state_dim + state_dim)
        ])

        self.next_state_tfpd = tfp.layers.DistributionLambda(
            make_distribution_fn=lambda t: tfp.distributions.Normal(t[0], t[1]))

    def init(self):
        if self.use_extra_data:
            self(tf.keras.Input(shape=(self.state_dim + 2,)),
                 tf.keras.Input(shape=(self.action_dim,)))
        else:
            self(tf.keras.Input(shape=(self.state_dim,)),
                 tf.keras.Input(shape=(self.action_dim,)))

    def call(self, state, action):
        next_state = self.dense(tf.concat([state, action], -1))
        mean, logstd = tf.split(next_state, num_or_size_splits=2, axis=-1)
        next_state_dist = self.next_state_tfpd([mean, tf.exp(logstd)])

        return next_state_dist

    def extra_obs(self, obs_list):
        return obs_list[0][..., -2:]


class ModelReward(m.ModelBaseReward):
    def __init__(self, state_dim, use_extra_data):
        super().__init__(state_dim, use_extra_data)

        self.dense = tf.keras.Sequential([
            tf.keras.layers.Dense(128, activation=tf.nn.relu),
            tf.keras.layers.Dense(128, activation=tf.nn.relu),
            tf.keras.layers.Dense(1)
        ])

    def call(self, state):
        reward = self.dense(state)

        return reward


class ModelObservation(m.ModelBaseObservation):
    def __init__(self, state_dim, obs_dims, use_extra_data):
        super().__init__(state_dim, obs_dims, use_extra_data)

        self.dense = tf.keras.Sequential([
            tf.keras.layers.Dense(128, activation=tf.nn.relu),
            tf.keras.layers.Dense(128, activation=tf.nn.relu),
            tf.keras.layers.Dense(53)
        ])

    def call(self, state):
        obs = self.dense(state)

        return obs

    def get_loss(self, state, obs_list):
        approx_obs = self(state)

        obs = obs_list[0]
        if not self.use_extra_data:
            obs = obs[..., :-2]

        return tf.reduce_mean(tf.square(approx_obs - obs))


class ModelRep(m.ModelBaseGRURep):
    def __init__(self, obs_dims, action_dim):
        super().__init__(obs_dims, action_dim, rnn_units=16)

        self.dense = tf.keras.Sequential([
            tf.keras.layers.Dense(128, activation=tf.nn.relu)
        ])

    def call(self, obs_list, pre_action, rnn_state):
        rnn_obs = tf.concat([obs_list[0][..., :5], pre_action], axis=-1)
        buoy_obs = obs_list[0][..., 5:-2]

        outputs, next_rnn_state = self.gru(rnn_obs, initial_state=rnn_state)

        state = tf.concat([outputs, self.dense(buoy_obs)], axis=-1)

        return state, next_rnn_state


class ModelQ(m.ModelContinuousQ):
    def __init__(self, state_dim, action_dim):
        super().__init__(state_dim, action_dim,
                         state_n=128, state_depth=2,
                         action_n=128, action_depth=2,
                         dense_n=128, dense_depth=3)


class ModelPolicy(m.ModelContinuousPolicy):
    def __init__(self, state_dim, action_dim):
        super().__init__(state_dim, action_dim,
                         dense_n=128, dense_depth=2,
                         mean_n=128, mean_depth=2,
                         logstd_n=128, logstd_depth=2)
