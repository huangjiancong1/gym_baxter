# Rethink Baxter Robot with OpenAI Baselines
## Setup Instructions:
1. Install `mujoco-py 1.50` and `baselines`
2. `pip uninstall gym`
3. `cd gym_baxter && pip install -e .`

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

### Avaliable trained policy with HER 
