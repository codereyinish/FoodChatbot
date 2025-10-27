<div id="top">

<!-- HEADER STYLE: CLASSIC -->
<div align="center">

<img src="readmeai/assets/logos/purple.svg" width="30%" style="position: relative; top: 0; right: 0;" alt="Project Logo"/>

# FOODCHATBOT.GIT

<em>Order food effortlessly with intelligent chatbot assistance.</em>

<!-- BADGES -->
<img src="https://img.shields.io/github/license/codereyinish/FoodChatbot.git?style=default&logo=opensourceinitiative&logoColor=white&color=0080ff" alt="license">
<img src="https://img.shields.io/github/last-commit/codereyinish/FoodChatbot.git?style=default&logo=git&logoColor=white&color=0080ff" alt="last-commit">
<img src="https://img.shields.io/github/languages/top/codereyinish/FoodChatbot.git?style=default&color=0080ff" alt="repo-top-language">
<img src="https://img.shields.io/github/languages/count/codereyinish/FoodChatbot.git?style=default&color=0080ff" alt="repo-language-count">

<!-- default option, no dependency badges. -->


<!-- default option, no dependency badges. -->

</div>
<br>

---

## Table of Contents

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
- [Features](#features)
- [Project Structure](#project-structure)
    - [Project Index](#project-index)
- [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Usage](#usage)
    - [Testing](#testing)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Overview

FoodChatbot.git simplifies the creation and management of a food ordering chatbot with a robust backend.

**Why FoodChatbot.git?**

This project streamlines the development of food ordering chatbots, offering key features such as:

- **🔍 Seamless Package Management:** Define dependencies effortlessly for smooth package handling.
- **🚀 Efficient Database Schema:** Automated calculations via triggers for streamlined operations.
- **💾 Quick Database Setup:** SQL dump files for easy database initialization.
- **🌐 FastAPI-based Backend:** Rapid development of a responsive chatbot interface.

---

## Features

|      | Component       | Details                              |
| :--- | :-------------- | :----------------------------------- |
| ⚙️  | **Architecture**  | <ul><li>Follows a **MVC** design pattern</li><li>Separation of concerns between models, views, and controllers</li></ul> |
| 🔩 | **Code Quality**  | <ul><li>Consistent code formatting using **Black**</li><li>Extensive use of type hints with **Pydantic** for data validation</li></ul> |
| 📄 | **Documentation** | <ul><li>Comprehensive inline code comments explaining complex logic</li><li>README.md with setup instructions and API endpoints documented</li></ul> |
| 🔌 | **Integrations**  | <ul><li>Integration with **MySQL** database using **mysql-connector-python**</li><li>API endpoints exposed using **FastAPI** framework</li></ul> |
| 🧩 | **Modularity**    | <ul><li>Modular structure with reusable components like **exceptiongroup** for error handling</li><li>Separate modules for different functionalities like user authentication, food recommendation</li></ul> |
| 🧪 | **Testing**       | <ul><li>Unit tests for critical functions using **pytest**</li><li>Integration tests for API endpoints using **pytest** and **FastAPI TestClient**</li></ul> |
| ⚡️  | **Performance**   | <ul><li>Asynchronous handling of requests using **FastAPI** and **uvicorn** for improved performance</li><li>Caching mechanisms implemented for frequently accessed data</li></ul> |
| 🛡️ | **Security**      | <ul><li>Input validation using **Pydantic** to prevent injection attacks</li><li>Secure handling of sensitive data like passwords using environment variables</li></ul> |
| 📦 | **Dependencies**  | <ul><li>Dependencies managed using **pip** and **conda** with clear specifications in **requirements.txt** and **environment.yml**</li><li>Key dependencies include **FastAPI**, **Pydantic**, **mysql-connector-python**</li></ul> |

---

## Project Structure

```sh
└── FoodChatbot.git/
    ├── app
    │   ├── __init__.py
    │   ├── dbOperations.py
    │   ├── generichelper.py
    │   └── main.py
    ├── database
    │   ├── README.md
    │   ├── backup
    │   └── schema.sql
    ├── environment.yml
    └── requirements.txt
```

### Project Index

<details open>
	<summary><b><code>FOODCHATBOT.GIT/</code></b></summary>
	<!-- __root__ Submodule -->
	<details>
		<summary><b>__root__</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ __root__</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/codereyinish/FoodChatbot.git/blob/master/requirements.txt'>requirements.txt</a></b></td>
					<td style='padding: 8px;'>Define project dependencies in requirements.txt for seamless package management.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/codereyinish/FoodChatbot.git/blob/master/environment.yml'>environment.yml</a></b></td>
					<td style='padding: 8px;'>- Define the project environment requirements using the provided <code>environment.yml</code> file<br>- Specify dependencies like Python 3.11, FastAPI, and MySQL connector<br>- Ensure the necessary packages are installed for the chatbot functionality to run smoothly.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- database Submodule -->
	<details>
		<summary><b>database</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ database</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/codereyinish/FoodChatbot.git/blob/master/database/schema.sql'>schema.sql</a></b></td>
					<td style='padding: 8px;'>- Define database schema for menu items, orders, and order tracking<br>- Implement triggers to calculate total price for orders and assign status for order tracking upon insertion.</td>
				</tr>
			</table>
			<!-- backup Submodule -->
			<details>
				<summary><b>backup</b></summary>
				<blockquote>
					<div class='directory-path' style='padding: 8px 0; color: #666;'>
						<code><b>⦿ database.backup</b></code>
					<table style='width: 100%; border-collapse: collapse;'>
					<thead>
						<tr style='background-color: #f8f9fa;'>
							<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
							<th style='text-align: left; padding: 8px;'>Summary</th>
						</tr>
					</thead>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/codereyinish/FoodChatbot.git/blob/master/database/backup/foodDatabase_full_dump_v2_20251016.sql'>foodDatabase_full_dump_v2_20251016.sql</a></b></td>
							<td style='padding: 8px;'>- Generate a SQL dump file containing tables for menu items, order tracking, and orders<br>- Includes table structures and sample data for each table<br>- Triggers are defined to calculate total prices and fill order statuses automatically<br>- Additionally, a stored procedure is provided to insert order items based on order ID, food item name, and quantity.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/codereyinish/FoodChatbot.git/blob/master/database/backup/foodDatabase_full_dump_v1_20251016.sql'>foodDatabase_full_dump_v1_20251016.sql</a></b></td>
							<td style='padding: 8px;'>- Generate a SQL dump file containing tables for menu items, order tracking, and orders<br>- Includes table structures and sample data for menu items and orders<br>- Implements triggers and procedures for calculating total prices and inserting order items<br>- The file serves as a comprehensive snapshot of the database schema and initial data for the project.</td>
						</tr>
					</table>
				</blockquote>
			</details>
		</blockquote>
	</details>
	<!-- app Submodule -->
	<details>
		<summary><b>app</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ app</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/codereyinish/FoodChatbot.git/blob/master/app/dbOperations.py'>dbOperations.py</a></b></td>
					<td style='padding: 8px;'>- Manage database operations for orders, including inserting items, retrieving order IDs, calculating total prices, validating tracking IDs, and extracting saved orders<br>- Utilizes MySQL connection and error handling to ensure data integrity.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/codereyinish/FoodChatbot.git/blob/master/app/generichelper.py'>generichelper.py</a></b></td>
					<td style='padding: 8px;'>- Generate a fulfillment message for an order, including item quantities<br>- Remove items from an order based on session ID<br>- Validate session ID and retrieve the order<br>- Check if an item is in the order list<br>- Convert a list to a string<br>- Derive a track ID from the output context.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/codereyinish/FoodChatbot.git/blob/master/app/main.py'>main.py</a></b></td>
					<td style='padding: 8px;'>- Implement a FastAPI-based backend for a food ordering chatbot<br>- Functions handle adding, removing, resetting orders, displaying carts, completing orders, tracking orders, and displaying tracked items<br>- The code interacts with a database for order storage and retrieval<br>- The main file, <code>main.py</code>, serves as the webhook handler for processing user requests and intents.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>

---

## Getting Started

### Prerequisites

This project requires the following dependencies:

- **Programming Language:** SQL
- **Package Manager:** Pip, Conda

### Installation

Build FoodChatbot.git from the source and intsall dependencies:

1. **Clone the repository:**

    ```sh
    ❯ git clone https://github.com/codereyinish/FoodChatbot.git
    ```

2. **Navigate to the project directory:**

    ```sh
    ❯ cd FoodChatbot.git
    ```

3. **Install the dependencies:**

<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![pip][pip-shield]][pip-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [pip-shield]: None -->
	<!-- [pip-link]: None -->

	**Using [pip](None):**

	```sh
	❯ echo 'INSERT-INSTALL-COMMAND-HERE'
	```
<!-- SHIELDS BADGE CURRENTLY DISABLED -->
	<!-- [![conda][conda-shield]][conda-link] -->
	<!-- REFERENCE LINKS -->
	<!-- [conda-shield]: None -->
	<!-- [conda-link]: None -->

	**Using [conda](None):**

	```sh
	❯ echo 'INSERT-INSTALL-COMMAND-HERE'
	```

### Usage

Run the project with:

**Using [pip](None):**
```sh
echo 'INSERT-RUN-COMMAND-HERE'
```
**Using [conda](None):**
```sh
echo 'INSERT-RUN-COMMAND-HERE'
```

### Testing

Foodchatbot.git uses the {__test_framework__} test framework. Run the test suite with:

**Using [pip](None):**
```sh
echo 'INSERT-TEST-COMMAND-HERE'
```
**Using [conda](None):**
```sh
echo 'INSERT-TEST-COMMAND-HERE'
```

---

## Roadmap

- [X] **`Task 1`**: <strike>Implement feature one.</strike>
- [ ] **`Task 2`**: Implement feature two.
- [ ] **`Task 3`**: Implement feature three.

---

## Contributing

- **💬 [Join the Discussions](https://github.com/codereyinish/FoodChatbot.git/discussions)**: Share your insights, provide feedback, or ask questions.
- **🐛 [Report Issues](https://github.com/codereyinish/FoodChatbot.git/issues)**: Submit bugs found or log feature requests for the `FoodChatbot.git` project.
- **💡 [Submit Pull Requests](https://github.com/codereyinish/FoodChatbot.git/blob/main/CONTRIBUTING.md)**: Review open PRs, and submit your own PRs.

<details closed>
<summary>Contributing Guidelines</summary>

1. **Fork the Repository**: Start by forking the project repository to your github account.
2. **Clone Locally**: Clone the forked repository to your local machine using a git client.
   ```sh
   git clone https://github.com/codereyinish/FoodChatbot.git
   ```
3. **Create a New Branch**: Always work on a new branch, giving it a descriptive name.
   ```sh
   git checkout -b new-feature-x
   ```
4. **Make Your Changes**: Develop and test your changes locally.
5. **Commit Your Changes**: Commit with a clear message describing your updates.
   ```sh
   git commit -m 'Implemented new feature x.'
   ```
6. **Push to github**: Push the changes to your forked repository.
   ```sh
   git push origin new-feature-x
   ```
7. **Submit a Pull Request**: Create a PR against the original project repository. Clearly describe the changes and their motivations.
8. **Review**: Once your PR is reviewed and approved, it will be merged into the main branch. Congratulations on your contribution!
</details>

<details closed>
<summary>Contributor Graph</summary>
<br>
<p align="left">
   <a href="https://github.com{/codereyinish/FoodChatbot.git/}graphs/contributors">
      <img src="https://contrib.rocks/image?repo=codereyinish/FoodChatbot.git">
   </a>
</p>
</details>

---

## License

Foodchatbot.git is protected under the [LICENSE](https://choosealicense.com/licenses) License. For more details, refer to the [LICENSE](https://choosealicense.com/licenses/) file.

---

## Acknowledgments

- Credit `contributors`, `inspiration`, `references`, etc.

<div align="right">

[![][back-to-top]](#top)

</div>


[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
