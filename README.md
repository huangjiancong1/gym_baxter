# Mujoco Simulation of [Rethink Baxter Robot](http://www.mujoco.org/forum/index.php?resources/baxter.17/)
## Setup Instructions:
1. Install [mujoco-py 1.50](https://github.com/openai/mujoco-py)`8702dd`, [gym](https://github.com/openai/gym)`220ae8` and [baselines](https://github.com/openai/baselines)`ba2b01`
2. `pip uninstall gym`
3. `git clone https://github.com/huangjiancong1/gym_baxter.git`
4. `cd gym_baxter && pip install -e .`

## Examples:
#### BaxterPush:
```
python -m baselines.run --alg=her --env=BaxterPush-v1 --num_timesteps=0 --load_path=/$PATH/policy --play
```
#### BaxterPickupAnd:
```
python -m baselines.run --alg=her --env=BaxterPickAndPlace-v1 --num_timesteps=0 --load_path=/$PATH/policy --play
```
#### BaxterGolf:
```
python -m baselines.run --alg=her --env=BaxterGolf-v1 --num_timesteps=0 --load_path=/$PATH/policy --play
```

### Available trained policy with HER 
Google Driver: https://drive.google.com/file/d/1R0A9YFQciM5rR0s6MQbEWLmw4yWu0Eux/view?usp=sharing

Baidu NetDisk: https://pan.baidu.com/s/1BSO0rAul9BYKpQH0zOypmw  pw:49es
