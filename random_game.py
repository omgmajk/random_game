import pandas as pd

df_games = pd.read_excel("games.xlsx")

random_game = df_games.sample(n=1)

random_game_string = random_game.to_string(buf=None, columns=None, col_space=None, header=True, index=True, na_rep='NaN', formatters=None, float_format=None, sparsify=None, index_names=True, justify=None, max_rows=None, max_cols=None, show_dimensions=False, decimal='.', line_width=None, min_rows=None, max_colwidth=None, encoding=None)

#print(random_game["Game"])
print(random_game_string)
