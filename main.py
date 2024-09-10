import argparse
from PIL import Image
import torch
from diffusers.utils import check_min_version
from controlnet_flux import FluxControlNetModel
from pipeline_flux_controlnet_inpaint import FluxControlNetInpaintingPipeline

check_min_version("0.30.2")

def main(image_path, mask_path, prompt):
    controlnet = FluxControlNetModel.from_pretrained("alimama-creative/FLUX.1-dev-Controlnet-Inpainting-Alpha", torch_dtype=torch.bfloat16)
    pipe = FluxControlNetInpaintingPipeline.from_pretrained(
        "black-forest-labs/FLUX.1-dev",
        controlnet=controlnet,
        torch_dtype=torch.bfloat16
    ).to("cuda")
    
    size = (768, 768)
    image = Image.open(image_path).convert("RGB").resize(size)
    mask = Image.open(mask_path).convert("RGB").resize(size)

    generator = torch.Generator(device="cuda").manual_seed(48)
    result = pipe(
        prompt=prompt,
        height=size[1],
        width=size[0],
        control_image=image,
        control_mask=mask,
        num_inference_steps=28,
        generator=generator,
        controlnet_conditioning_scale=0.95,
        guidance_scale=3.5,
        negative_prompt="",
        true_guidance_scale=3.5
    ).images[0]
    
    result.save('flux_inpaint.png')
    print("Successfully inpainted image")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Image Inpainting Program")
    parser.add_argument("-i", "--image", required=True, help="Path to the input image")
    parser.add_argument("-m", "--mask", required=True, help="Path to the input mask")
    parser.add_argument("-p", "--prompt", required=True, help="Prompt for inpainting")
    args = parser.parse_args()
    main(args.image, args.mask, args.prompt)
