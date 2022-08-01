import pandas as pd

def read_notes(path_to_file):
    return pd.read_csv(path_to_file)

def save_to_csv(df, path_to_file):
    df.to_csv(path_to_file, index=False)

def add_note(df, film_name, note, rating):
    if 1<=rating<=5:
        df.loc[len(df.index)] = [film_name, note, rating]
    else:
        raise Exception("Sorry, rating should be in range 1-5")

def add_note_and_save(df, film_name, note, rating, path_to_file):
    if 1<=rating<=5:
        df.loc[len(df.index)] = [film_name, note, rating]
        save_to_csv(df, path_to_file)
    else:
        raise Exception("Sorry, rating should be in range 1-5")

def remove_note(df, row, path_to_file):
    df = df.drop(df.index[row-1])
    save_to_csv(df, path_to_file)

def remove_note_and_save(df, row):
    df = df.drop(df.index[row-1])

def print_all_notes(df):
    print(df.to_markdown())

def get_the_highest_rating(df):
    return df['rating'].nlargest(n=5)

def get_the_lowest_rating(df):
    return df['rating'].nmallest(n=5)

def get_the_avarage_rating():
    return df['rating'].mean()
