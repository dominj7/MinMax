run:
	python3 main.py
	rm -r __pycache__
	clear
	
exe:
	pyinstaller -F -w -n TicTacToe main.py
	mv ./dist/TicTacToe ./
	rm -r build dist __pycache__ TicTacToe.spec
	clear
