🪸 Nautilus Project – Diving Log Desktop Application

A desktop application developed in Python to manage diving log entries.
The project follows the MVC (Model-View-Controller) architecture and uses SQLite for data persistence.

📌 Description

Nautilus allows users to create, view, update, and delete diving records.
All data is stored locally in a SQLite database.
The application includes input validation and dynamic filtering through a graphical interface.

🛠 Technologies Used

_Python 3

_Tkinter (GUI)

_SQLite3

_Regular Expressions

_MVC Architecture

🚀 Features

_Create new dive entries

_Update existing records

_Delete records

_View all dives

_Search by date or location

_Input validation

_Local database persistence

📂 Project Structure
Proyecto_Nautilus_Buceo.py

modelo_buceo.py

controlador_buceo.py

vista_buceo.py

buceo.db

▶️ How to Run
python Proyecto_Nautilus_Buceo.py
🧠 Architecture

The application is structured following the MVC pattern:

Model: Handles database operations (SQLite)

View: Tkinter graphical interface

Controller: Connects user actions with business logic
