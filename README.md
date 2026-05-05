1.  **Clone repository**
    ```bash
    git clone https://github.com/your-username/python-chess-ai.git
    cd python-chess-ai
    ```

3.  **Create a virtual environment (Optional but recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

4.  **Install dependencies:**
    ```bash
    pip install pygame
    ```

5.  **Run the game:**
    ```bash
    python main.py
    ```

## 🎮 How to Play

1.  Launch the game.
2.  **Select Mode:** Choose between "Player vs Player" or "Player vs AI."
3.  **Move Pieces:** Click on a piece to see valid moves, then click the destination square.
4.  **Special Moves:** The game will automatically handle logic for castling and promotions.

## 🤖 AI Roadmap

The AI is currently being developed using the following milestones:
- [x] Basic move generation.
- [ ] Piece-Square tables for board evaluation.
- [ ] Implementation of **Minimax Algorithm**.
- [ ] Optimization using **Alpha-Beta Pruning**.
- [ ] Move ordering and opening book integration.

## 🤝 Contributing

Contributions are welcome! If you have ideas for improving the AI or adding new UI features:
1. Fork the Project.
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`).
3. Commit your Changes (`git commit -m 'Add comment'`)
4. Push your Changes for review (`git push origin main`)
