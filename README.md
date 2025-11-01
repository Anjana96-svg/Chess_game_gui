# Chess_game_gui
PyQt5 Chess — Interactive Chessboard with Move Validation

Developed a desktop-based interactive chess game using Python and PyQt5, combining object-oriented design and graphical user interface programming. The system allows two players to play a complete chess match with rule-based movement validation, turn management, and real-time board updates. 


⚙️ Key Features

Interactive GUI: Built an 8×8 chessboard grid using PyQt5 GridLayout, with alternating tile colors and piece icons rendered dynamically.

Rule-Based Move Validation: Implemented logic for all chess pieces (Pawn, Rook, Knight, Bishop, Queen, King) including diagonal, straight, and L-shaped movements.

Turn Handling: Integrated automatic turn switching between White and Black players.

Collision Detection: Added checks for valid captures and movement restrictions using path obstruction logic.

Modular Design: Separated game logic (chess_logic.py) from GUI (chess_gui.py) following Object-Oriented Programming (OOP) principles.

Scalable Architecture: Easily extendable for advanced features like check detection, castling, or AI opponent integration.                                                 

🧩 Tech Stack

Programming Language: Python

Framework: PyQt5

Concepts Used: OOP, Event Handling, GUI Design, Logical Validation, Data Structures

Assets: Custom chess piece icons rendered from the src/images directory                                                        


🚀 How It Works

Board Setup: Initializes an 8×8 grid with chess pieces placed in their standard starting positions.

Move Execution: Users click the source and destination squares; the system validates the move before updating the board.

Validation Logic: Checks movement type, direction, obstruction, and color before confirming a move.

UI Update: The interface refreshes automatically with the new piece positions and highlights the current turn.            


<img width="831" height="727" alt="chess game " src="https://github.com/user-attachments/assets/e8dc511c-2e1b-4d12-ab46-e4598dd5bf6a" />







