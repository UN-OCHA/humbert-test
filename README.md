# Create own model for RW jobs

Make sure you have at least 25GB free space.

## External links

- https://github.com/the-deep-nlp/classifier-trainer
- https://www.reddit.com/r/MachineLearning/comments/y8qs5m/r_hardware_to_train_language_representation_model/

## Docker image

Run `./build.sh` to create the image

## Data format

csv files with 2 columns: `excerpt` and `target_classification`

- `excerpt` is a blob of text
- `target_classification` is an array of terms, ex: `["Food and Nutrition","Safety and Security"]`

## Train it

Uses `base_architecture` with 500 samples.

Run `./train.sh` takes around 15 minutes to run

## Test it

Run `./testing.sh`, will output something like

```
                                                                         tag  precision  recall  f_score positive_examples_proportion
Agriculture                                                      Agriculture      0.000   0.000    0.000                          NaN
Camp Coordination and Camp Management  Camp Coordination and Camp Management      0.000   0.000    0.000                          NaN
Climate Change and Environment                Climate Change and Environment      0.000   0.000    0.000                          NaN
Coordination                                                    Coordination      0.333   0.500    0.400                          NaN
Disaster Management                                      Disaster Management      0.000   0.000    0.000                          NaN
Education                                                          Education      0.000   0.000    0.000                          NaN
Food and Nutrition                                        Food and Nutrition      0.333   1.000    0.500                          NaN
Gender                                                                Gender      0.000   0.000    0.000                          NaN
HIV/Aids                                                            HIV/Aids      0.083   1.000    0.154                          NaN
Health                                                                Health      0.429   1.000    0.600                          NaN
Mine Action                                                      Mine Action      0.000   0.000    0.000                          NaN
Peacekeeping and Peacebuilding                Peacekeeping and Peacebuilding      0.429   0.750    0.545                          NaN
Protection and Human Rights                      Protection and Human Rights      0.857   0.750    0.800                          NaN
Recovery and Reconstruction                      Recovery and Reconstruction      0.062   1.000    0.118                          NaN
Safety and Security                                      Safety and Security      1.000   0.667    0.800                          NaN
Shelter and Non-Food Items                        Shelter and Non-Food Items      0.059   1.000    0.111                          NaN
Water Sanitation Hygiene                            Water Sanitation Hygiene      0.000   0.000    0.000                          NaN
0                                                                     mean->      0.211   0.451    0.237                            -
0                                                                     mean->      0.211   0.451    0.237                            -
```
