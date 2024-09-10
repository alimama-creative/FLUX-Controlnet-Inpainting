
## FLUX1.D Controlnet Inpainting

This repository provides a Inpainting ControlNet checkpoint for ![FLUX.1-dev](https://huggingface.co/black-forest-labs/FLUX.1-dev) model released by researchers from AlimamaCreative Tech Team.

## Model Cards

![SD3](images/sd3_compressed.png)

<center><i>a woman wearing a white jacket, black hat and black pants is standing in a field, the hat writes SD3</i></center>

![bucket_alibaba](images/bucket_ali_compressed.png )

<center><i>a person wearing a white shoe, carrying a white bucket with text "alibaba" on it</i></center>

![See our github]() for inference code.


# Comparison with SDXL-Inpainting

Compared with [SDXL-Inpainting](https://huggingface.co/diffusers/stable-diffusion-xl-1.0-inpainting-0.1)

From left to right: Input image, Masked image, SDXL inpainting, Ours.

![0](images/0_compressed.png)
<center><i>a tiger sitting on a park bench</i></center>

![1](images/0r_compressed.png)
<center><i>a dog sitting on a park bench</i></center>

![2](images/1_compressed.png)
<center><i>a young woman wearing a blue and pink floral dress</i></center>

![3](images/3_compressed.png)
<center><i>a woman wearing a white jacket, black hat and black pants is standing in a field, the hat writes SD3</i></center>

![4](images/5_compressed.png)
<center><i>an air conditioner hanging on the bedroom wall</i></center>

# Using with Diffusers

Install from source and Run

``` Shell
pip uninstall diffusers
pip install git+https://github.com/huggingface/diffusers
```

``` python

```


## Training Detail

The model was trained on 12M laion2B and internal source images for 80k steps at resolution 1024x1024. 

## Limitation
Due to the fact that only 1024*1024 pixel resolution was used during the training phase, the inference performs best at this size, with other sizes yielding suboptimal results.

## LICENSE
Our weights fall under the ![FLUX.1 [dev]](https://huggingface.co/black-forest-labs/FLUX.1-dev/blob/main/LICENSE.md) Non-Commercial License.