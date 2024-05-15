import sqlite3
import pandas as pd
import csv

def main():
    # Opprett en tilkobling til SQLite-databasen
    conn = opprett_tilkobling()

    # Opprett tabeller fra CSV-filer
    opprett_tabell_fra_csv(conn, 'postnummerregister.csv', 'postnummerregister')
    opprett_tabell_fra_csv(conn, 'randoms.csv', 'personer')
    # Lukk tilkoblingen til SQLite-databasen
    conn.close()

def opprett_tilkobling():
    # Opprett en tilkobling til SQLite-databasen
    conn = sqlite3.connect('database.db')
    # Returner tilkoblingsobjektet
    return conn

def opprett_tabell_fra_csv(conn, csv_filnavn, tabellnavn):
    # Last inn CSV-filen i en pandas DataFrame
    df = pd.read_csv(csv_filnavn)

    # Skriv dataene fra DataFrame til en ny SQLite-tabell
    df.to_sql(tabellnavn, conn, if_exists='replace', index=False)

if __name__ == "__main__":
    main()