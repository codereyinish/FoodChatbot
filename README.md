<!-- HEADER STYLE: CLASSIC -->
<p align="center">
  <img 
    src="https://github.com/codereyinish/FoodChatbot/blob/main/assets/khajaG_pic.png" 
    alt="KhajaG Logo" 
    style="width: 300px; border-radius: 25px;"
  >
</p>

    <h1 align="center">Not an ordinary chatbot</h1>
</p>
<p align="center">
    <em>Order food effortlessly with intelligent chatbot assistance.</em>
</p>

<p align="center">
	<img src="https://img.shields.io/badge/License-MIT-green?style=for-the-badge" alt="license">
	<img src="https://img.shields.io/github/last-commit/codereyinish/FoodChatbot?style=for-the-badge&logo=git&logoColor=white&color=2196F3" alt="last-commit">
	<img src="https://img.shields.io/github/languages/top/codereyinish/FoodChatbot?style=for-the-badge&color=FF9800" alt="repo-top-language">
	<img src="https://img.shields.io/github/languages/count/codereyinish/FoodChatbot?style=for-the-badge&color=9C27B0" alt="repo-language-count">
</p>

<em>Developed with the software and tools below.</em>
</p>
<p align="center">
  <img src="https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white" alt="Python">
  <img src="https://img.shields.io/badge/pyngrok-1DA1F2?style=flat&logo=ngrok&logoColor=white" alt="pyngrok">
  <img src="https://img.shields.io/badge/FastAPI-009688?style=flat&logo=fastapi&logoColor=white" alt="FastAPI">
  <img src="https://img.shields.io/badge/MySQL-4479A1?style=flat&logo=mysql&logoColor=white" alt="MySQL">
  <img src="https://img.shields.io/badge/Dialogflow-FF9800?style=flat&logo=dialogflow&logoColor=white" alt="Dialogflow">
  <img src="https://img.shields.io/badge/GitHub-181717?style=flat&logo=github&logoColor=white" alt="GitHub">
  <img src="https://img.shields.io/badge/PyCharm-21D789?style=flat&logo=pycharm&logoColor=white" alt="PyCharm">
  <img src="https://img.shields.io/badge/Notion-000000?style=flat&logo=notion&logoColor=white" alt="Notion">
</p>


<br>

<br><!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary><br>

[![🏁 Overview](https://img.shields.io/badge/🏁-Overview-blue)](#-overview)  
[![📂 Repository Structure](https://img.shields.io/badge/📂-Repository%20Structure-green)](#-repository-structure)  
[![🧠 Modules](https://img.shields.io/badge/🧠-Modules-yellow)](#-modules)  
[![🚀 Getting Started](https://img.shields.io/badge/🚀-Getting%20Started-orange)](#-getting-started)  
&nbsp;&nbsp;&nbsp;&nbsp;[![🧰 Installation](https://img.shields.io/badge/🧰-Installation-lightgrey)](#-installation)  
&nbsp;&nbsp;&nbsp;&nbsp;[![⚡ Usage](https://img.shields.io/badge/⚡-Usage-lightgrey)](#-usage)  
[![🛣️ Project Roadmap](https://img.shields.io/badge/🛣️-Project%20Roadmap-9cf)](#-project-roadmap)  
[![🤝 Contributing](https://img.shields.io/badge/🤝-Contributing-ff69b4)](#-contributing)  
[![📜 License](https://img.shields.io/badge/📜-License-lightblue)](#-license)  
[![🌟 Acknowledgments](https://img.shields.io/badge/🌟-Acknowledgments-yellowgreen)](#-acknowledgments)

</details>

<hr>
</details>

<hr>

## 🏁 Overview

KhajaG is a lightweight food ordering chatbot built using Dialogflow ES, FastAPI , ngrok, and a local MySQL database.
The system connects Dialogflow intents to a FastAPI backend through a secure ngrok tunnel, enabling real-time order handling and database interaction.




## 📂 Repository Structure

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
    ├── chatbot_setup
    │   └── KhajaG_dialogflow.zip
    ├── environment.yml
    └── requirements.txt

```

### 🧠 Modules

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
					<td style='padding: 8px;'><b><a href='https://github.com/codereyinish/FoodChatbot/blob/master/requirements.txt'>requirements.txt</a></b></td>
					<td style='padding: 8px;'>Define project dependencies in requirements.txt for seamless package management.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/codereyinish/FoodChatbot/blob/master/environment.yml'>environment.yml</a></b></td>
					<td style='padding: 8px;'>- Define the project environment requirements using the provided <code>environment.yml</code> file<br>- Specify dependencies like Python 3.11, FastAPI, and MySQL connector<br>- Ensure the necessary packages are installed for the chatbot functionality to run smoothly.</td>
				</tr>
			</table>
		</blockquote>
	</details>
	<!-- chatbot_setup Submodule -->
	<details>
		<summary><b>chatbot_setup</b></summary>
		<blockquote>
			<div class='directory-path' style='padding: 8px 0; color: #666;'>
				<code><b>⦿ chatbot_setup</b></code>
			<table style='width: 100%; border-collapse: collapse;'>
			<thead>
				<tr style='background-color: #f8f9fa;'>
					<th style='width: 30%; text-align: left; padding: 8px;'>File Name</th>
					<th style='text-align: left; padding: 8px;'>Summary</th>
				</tr>
			</thead>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/codereyinish/FoodChatbot/blob/master/chatbot_setup/KhajaG_dialogflow.zip'>KhajaG_dialogflow.zip</a></b></td>
					<td style='padding: 8px;'>- Exported <code>Dialogflow ES</code> agent used for the KhajaG chatbot<br>- Includes intents, entities, training phrases, and fulfillment settings<br>- Can be imported directly into Dialogflow Console to replicate the chatbot.</td>
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
					<td style='padding: 8px;'><b><a href='https://github.com/codereyinish/FoodChatbot/blob/master/database/schema.sql'>schema.sql</a></b></td>
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
							<td style='padding: 8px;'><b><a href='https://github.com/codereyinish/FoodChatbot/blob/master/database/backup/foodDatabase_full_dump_v2_20251016.sql'>foodDatabase_full_dump_v2_20251016.sql</a></b></td>
							<td style='padding: 8px;'>- Generate a SQL dump file containing tables for menu items, order tracking, and orders<br>- Includes table structures and sample data for each table<br>- Triggers are defined to calculate total prices and fill order statuses automatically<br>- Additionally, a stored procedure is provided to insert order items based on order ID, food item name, and quantity.</td>
						</tr>
						<tr style='border-bottom: 1px solid #eee;'>
							<td style='padding: 8px;'><b><a href='https://github.com/codereyinish/FoodChatbot/blob/master/database/backup/foodDatabase_full_dump_v1_20251016.sql'>foodDatabase_full_dump_v1_20251016.sql</a></b></td>
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
					<td style='padding: 8px;'><b><a href='https://github.com/codereyinish/FoodChatbot/blob/master/app/dbOperations.py'>dbOperations.py</a></b></td>
					<td style='padding: 8px;'>- Manage database operations for orders, including inserting items, retrieving order IDs, calculating total prices, validating tracking IDs, and extracting saved orders<br>- Utilizes MySQL connection and error handling to ensure data integrity.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/codereyinish/FoodChatbot/blob/master/app/generichelper.py'>generichelper.py</a></b></td>
					<td style='padding: 8px;'>- Generate a fulfillment message for an order, including item quantities<br>- Remove items from an order based on session ID<br>- Validate session ID and retrieve the order<br>- Check if an item is in the order list<br>- Convert a list to a string<br>- Derive a track ID from the output context.</td>
				</tr>
				<tr style='border-bottom: 1px solid #eee;'>
					<td style='padding: 8px;'><b><a href='https://github.com/codereyinish/FoodChatbot/blob/master/app/main.py'>main.py</a></b></td>
					<td style='padding: 8px;'>- Implement a FastAPI-based backend for a food ordering chatbot<br>- Functions handle adding, removing, resetting orders, displaying carts, completing orders, tracking orders, and displaying tracked items<br>- The code interacts with a database for order storage and retrieval<br>- The main file, <code>main.py</code>, serves as the webhook handler for processing user requests and intents.</td>
				</tr>
			</table>
		</blockquote>
	</details>
</details>



## 🚀 Getting Started

### 🧭 Prerequisites

Before running the project, make sure you have:

- **Programming Language:** SQL  
- **Package Manager:** `pip` or `conda`  
- **Python Version:** 3.10 or higher  
- **Database:** MySQL (installed and running locally or remotely)

> 💡 **Tip:** Make sure MySQL service is running before starting the app.


## 🧰 Installation Guide

Build **FoodChatbot** from the source and set up the environment step by step 🧭

---

1. **Clone the Repository:**

    ```sh
    ❯ git clone https://github.com/codereyinish/FoodChatbot.git
    ```

2. **Navigate to the Project Folder:**

    ```sh
    ❯ cd FoodChatbot
    ```

3. **Install the Dependencies:**

    **Using pip:**
    ```sh
    ❯ pip install -r requirements.txt
    ```

    **Using conda:**
    ```sh
    ❯ conda env create -f environment.yml
    ❯ conda activate chatbot_env
    ```

4. **Set Up MySQL Database 🛢️**

    - Make sure MySQL is installed and running.  
    - Create a new database:
    ```sql
    CREATE DATABASE mb_eats;
    ```
    - Import the schema file:
    ```sh
    ❯ mysql -u root -p mb_eats < database/schema.sql
    ```
    - Create a `.env` file in the project root:
    ```env
    host=localhost
    user=root
    db_password=yourpassword
    database=mb_eats
    ```

    > 💡 **Tip:** Keep your `.env` file secure and never commit it to GitHub.

---

5. **Import the Dialogflow Agent 🤖**

   - Go to [Dialogflow Console](https://dialogflow.cloud.google.com).
   - Create a **new agent** (or use an existing one).
   - Click the ⚙️ **gear icon** next to the agent name → go to **Export and Import**.
   - Choose **“Import from ZIP”** and upload:
     ```
     chatbot_setup/KhajaG_dialogflow.zip
     ```
   - Once imported, all intents, entities, and fulfillment settings will be ready to use.
   - In Dialogflow → **Fulfillment**, set your webhook URL to:
     ```
     https://<your-ngrok-or-cloud-run-url>/webhook
     ```
   - Enable the webhook for all required intents.

> 📝 This step makes your chatbot respond exactly like the original KhajaG setup.

---

6. **Set Up Ngrok (Optional for Webhooks) 🌐**

    - Download and install [ngrok](https://ngrok.com)  
    - Authenticate your ngrok account:
    ```sh
    ❯ ngrok config add-authtoken YOUR_TOKEN
    ```
    - Run ngrok to expose your FastAPI server:
    ```sh
    ❯ ngrok http 8000
    ```
    - Copy the **Forwarding URL** (e.g., `https://xxxx.ngrok.io`) and use it as your webhook URL in Dialogflow.

 ---

### ⚡ Usage

Run the project locally:

**Using pip: / conda: **
```sh
❯ uvicorn app.main:app --reload
```
---

## 🛣️ Project Roadmap]
- [🟠] **`Task 2`**: Deploy backend to **Google Cloud**  
  - Use **Cloud Run** or **App Engine**  
  - Connect to **Cloud SQL (MySQL)**  
  - Set up CI/CD  
  - Replace ngrok with secure HTTPS endpoint

- [🟡] **`Task 3`**: Move from **Dialogflow ES** to **Dialogflow CX**  
  - Better flow handling & state management  
  - Advanced routing and fallback control

- [🔵] **`Task 4`**: Build a **standalone chatbot widget**  
  - Website & app integration  
  - Branding support & live order tracking

- [⚡] **`Task 5`**: Scale for production  
  - Logging & monitoring  
  - Multi-tenant support  
  - Performance & security upgrades
---

## 🤝 Contributing

Contributions are always welcome to make **FoodChatbot** better 🚀  
If you want to be part of this journey of building a **Chatbot Developer Agency**, you can **DM me** 💬

- 🐛 **[Report Issues](https://github.com/codereyinish/FoodChatbot.git/issues)** — Found a bug or want a new feature.  
- 💡 **[Submit Pull Requests](https://github.com/codereyinish/FoodChatbot.git/blob/main/CONTRIBUTING.md)** — Contribute improvements.  
- 💬 **[Join Discussions](https://github.com/codereyinish/FoodChatbot.git/discussions)** — Share ideas, ask questions, or give feedback.

---

<details closed>
<summary>📌 Contributing Guidelines</summary>

1. **Fork the Repository** to your GitHub account.  
2. **Clone Locally**:
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
<summary>👥 Contributor Graph</summary>
<br>
<p align="center">
   <a href="https://github.com/codereyinish/FoodChatbot/graphs/contributors">
      <img src="https://contrib.rocks/image?repo=codereyinish/FoodChatbot" alt="Contributors Graph">
   </a>
</p>

<p align="center">
   💖 A big thank you to all the amazing contributors who helped shape this project!
</p>

<p align="center">
   <a href="https://github.com/codereyinish/FoodChatbot/graphs/contributors">View all contributors →</a>
</p>
</details>

---

## 🎗 License

[MIT-License](LICENSE)

---
## 🙏 Acknowledgments

This project was built with the help, guidance, and inspiration from amazing resources and people:

- 🎥 [**Dhaval Patel**](https://github.com/codebasics) — for the incredible [YouTube tutorial](https://youtu.be/2e5pQqBvGco?si=ZvkRKMfRrLTjg5DG) that guided the foundation of this chatbot project.

- ☕ Friends & collaborators who supported the idea and development of **FoodChatbot**.

> 💬 If you want to be part of this journey of building a **Chatbot Developer Agency**, you’re welcome to **DM me** and contribute 🤝

<div align="right">
	
[![][back-to-top]](#top)
	
</div>



[back-to-top]: https://img.shields.io/badge/-BACK_TO_TOP-151515?style=flat-square


---
