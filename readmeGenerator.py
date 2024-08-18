# 👉 py readmeGenerator.py

import os

# Boolean variable to control whether to prompt for the output directory
prompt_for_output_dir = (
    False  # Set to True if you want to be prompted for the directory
)


# Function to generate the README.md file content
def generate_readme(package_name, package_description, function_name):
    readme_template = f"""# @reliverse/addons: {package_name}

{package_description}

**Note:** [Additional Information: Include any specific notes or focuses for the package, such as whether it extends existing functionality or introduces new utilities.]

For detailed usage instructions, API documentation, and examples, please visit the [Reliverse Docs](https://reliverse.org) website. If the page for this package is missing, please notify us or consider contributing to add it.

## Installation

To install or update this package, run:

```bash
pnpm add @reliverse/{package_name}@latest
```

or with Bun:

```bash
bun add @reliverse/{package_name}@latest
```

## How to Use This Library

To use `@reliverse/{package_name}`, ensure that your project is set up as an ES module by including `"type": "module"` in your `package.json` file. Since this package is structured as an ES module, you'll need to use `import` statements instead of `require`.

Here's an example of how to import and use a function from this package:

```ts
import {{ {function_name} }} from "@reliverse/{package_name}";

const someFile = "path/to/file";

export async function exampleFunction() {{
  await {function_name}(someFile);
}}
```

Please refer to the source files located in the [`src` folder](https://github.com/reliverse/{package_name}/blob/main/src) to learn about the currently implemented functions.

This package adopts the ES module format, with files compiled to `dist/.js`. This aligns with the Node.js team's recent recommendations, encouraging the JavaScript/TypeScript community to transition to the ES module standard. If your project still requires CommonJS (CJS) support, you may fork this repository and modify the build process to generate `dist/.cjs` files. For guidance or community support, join the [Reliverse Discord community](https://discord.gg/C4Z46fHKQ8).

## Documentation and Support

If you encounter any issues, need help, or want to contribute, you can:

- Join the [Reliverse Discord community](https://discord.gg/C4Z46fHKQ8) to ask questions and engage with other users and developers.
- For usage instructions, API documentation, and examples, please visit the [Reliverse Docs](https://reliverse.org) website.
- Report bugs or suggest features by opening an issue on our [GitHub repository](https://github.com/reliverse/{package_name}/issues).

## Sponsors

*Love using this project? If you find it useful, I’d greatly appreciate a cup of coffee! By supporting this project, you'll gain access to Reliverse Pro, exclusive access to @reliverse/addons-pro, private repositories, pre-release downloads, and even the ability to influence project planning. Click on the donation platforms below to learn more. Thank you all for your support!*

**[We're Growing Fast! A Huge Thanks to All Our Supporters!](https://github.com/blefnk/relivator/stargazers)**

Developing something as ambitious as [@reliverse/addons](https://github.com/reliverse/addons) takes a huge amount of time, especially since the project is primarily developed by one person. The development could be significantly accelerated by bringing on additional developers. Therefore, @blefnk (Nazar Kornienko), the author of this project, would be immensely grateful to anyone who can contribute financially in any amount. A big thank you in advance to everyone who supports this effort!

**[Visit the "Donate to Relivator" page to see our current donors and learn more.](https://relivator.reliverse.org/donate)**

### 💚 [GitHub Sponsors](https://github.com/sponsors/blefnk) 🩵 [PayPal](https://paypal.me/blefony) 🧡 [Patreon](https://patreon.com/blefnk) 💛 [Buy Me a Coffee](https://buymeacoffee.com/blefnk) 🩷 [Ko-fi](https://ko-fi.com/blefnk)

## Contributing

We welcome contributions! If you’d like to contribute to the development of this package, please follow these steps:

1. **If you are a beginner:** Familiarize yourself with Git by following [The Detailed Git Guide](https://github.com/blefnk/relivator/blob/main/.github/GITGUIDE.md) created by @blefnk and @reliverse.
2. Fork this repository.
3. Create a new branch for your feature (e.g. `git checkout -b feature-branch`).
4. Make your changes in the new branch.
5. Commit your changes with a descriptive message (e.g. `git commit -m 'Add new feature'`).
6. Push your changes to your branch (e.g. `git push origin feature-branch`).
7. Open a [pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-pull-requests) for our review.

Please ensure that your code follows the existing code style and includes appropriate tests. Your code should successfully pass the `pnpm appts` command.

## License

This project is developed by [Reliverse](https://github.com/orgs/reliverse/repositories) and [@blefnk (Nazar Kornienko)](https://github.com/blefnk) and is licensed under the MIT License. For more information, please refer to the [LICENSE](./LICENSE) file.
"""
    return readme_template


# Function to save the README.md file
def save_readme(content, output_dir):
    output_path = os.path.join(output_dir, "README.md")
    if os.path.exists(output_path):
        overwrite = (
            input(
                f"README.md already exists in {output_dir}. Do you want to overwrite it? (y/n): "
            )
            .strip()
            .lower()
        )
        if overwrite != "y":
            print("Operation canceled. README.md was not overwritten.")
            return
    with open(output_path, "w", encoding="utf-8", newline="\n") as file:
        file.write(content)
    print(f"README.md has been generated and saved to {output_path}")


# Function to delete the script itself
def remove_script():
    script_path = os.path.abspath(__file__)
    delete = (
        input("Do you want to delete the readmeGenerator.py script? (y/n): ")
        .strip()
        .lower()
    )
    if delete == "y":
        os.remove(script_path)
        print(
            "\n- Please open the README.md file and make any additional changes."
            "\n- The readmeGenerator.py script has been deleted.\n"
        )

    else:
        print(
            "\n- Please open the README.md file and make any additional changes."
            "\n- The readmeGenerator.py script was not deleted."
            "\n- Please remove the readmeGenerator.py file manually before publishing the package.\n"
        )


# Main function to gather inputs and generate the README.md
def main():
    print("Welcome to the README.md Generator for @reliverse/addons packages!")

    package_name = input("Enter the package name (e.g., fs): ").strip()
    package_description = input("Enter a brief description of the package: ").strip()
    function_name = input(
        "Enter the name of a primary function in the package: "
    ).strip()

    # Determine the output directory
    if prompt_for_output_dir:
        output_dir = input(
            "Enter the directory where README.md should be saved: "
        ).strip()
    else:
        output_dir = os.path.abspath(os.path.dirname(__file__))

    # Generate the README.md content
    readme_content = generate_readme(package_name, package_description, function_name)

    # Save the README.md file
    save_readme(readme_content, output_dir)

    # Ask if the user wants to remove the script itself
    remove_script()


if __name__ == "__main__":
    main()
