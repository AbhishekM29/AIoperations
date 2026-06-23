import openai

def generate_animal_image(animal_name, output_file="animal.png"):
    prompt = f"Realistic image of a {animal_name}"

    response = openai.images.generate(
        model="gpt-image-1",
        prompt=prompt,
        size="512x512"
    )

    # Get the image URL
    image_url = response.data[0].url

    # Download the image
    import requests
    img_data = requests.get(image_url).content
    with open(output_file, "wb") as handler:
        handler.write(img_data)

    print(f"Image of {animal_name} saved as {output_file}")


# Example usage:
generate_animal_image("lion")
generate_animal_image("elephant")
