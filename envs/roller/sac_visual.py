import numpy as np
import tensorflow as tf
import tensorflow_probability as tfp

import algorithm.nn_models as m


class ModelRep(m.ModelBaseSimpleRep):
    def __init__(self, obs_dims):
        super().__init__(obs_dims)

        self.conv = tf.keras.Sequential([
            # tf.keras.layers.Conv2D(filters=32, kernel_size=8, strides=4, activation=tf.nn.relu),
            # tf.keras.layers.Conv2D(filters=64, kernel_size=4, strides=2, activation=tf.nn.relu),
            tf.keras.layers.Conv2D(filters=16, kernel_size=8, strides=4, activation=tf.nn.relu),
            tf.keras.layers.Conv2D(filters=32, kernel_size=4, strides=2, activation=tf.nn.relu),
            tf.keras.layers.Flatten(),
            tf.keras.layers.Dense(128, activation=tf.nn.relu),
            tf.keras.layers.Dense(64, activation=tf.nn.relu)
        ])

        self.dense = tf.keras.Sequential([
            tf.keras.layers.Dense(64, activation=tf.nn.relu),
        ])

    def call(self, obs_list):
        vis_obs = obs_list[0]
        vec_obs = obs_list[1]

        vis_obs = m.through_conv(vis_obs, self.conv)

        state = self.dense(tf.concat([vis_obs, vec_obs], -1))

        return state


class ModelQ(m.ModelContinuesQ):
    def __init__(self, state_dim, action_dim):
        super().__init__(state_dim, action_dim,
                         dense_n=128, dense_depth=2)


class ModelPolicy(m.ModelContinuesPolicy):
    def __init__(self, state_dim, action_dim):
        super().__init__(state_dim, action_dim,
                         dense_n=128, dense_depth=2)
