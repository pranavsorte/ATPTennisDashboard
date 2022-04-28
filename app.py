# from pickle import TRUE
from asyncio.windows_events import NULL
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
import psycopg2
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres::pranav@localhost/atp_tennis'

db = SQLAlchemy(app)

def get_db_connection():
    conn = psycopg2.connect(host='localhost',
                            database='atp_tennis',
                            user="postgres",
                            password='pranav')
    return conn
    
    
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/rankings', methods = ['GET','POST'])
def rankings():
    if request.method == 'POST':
        first_name = request.form['firstname']
        last_name = request.form['lastname']
        print(first_name,last_name)
        # print(db)
        
        conn = get_db_connection()
        cur = conn.cursor()
        # select A.name_first, A.name_last, B.rank, B.points from atp_rankings_current B, atp_players A where A.player_id = B.player_id AND A.name_first = 'Novak' AND A.name_last = 'Djokovic';
        query = "select A.name_first, A.name_last, B.rank, B.points from atp_rankings_current B, atp_players A where A.player_id = B.player_id AND A.name_first = '" + first_name + "' AND A.name_last = '" + last_name + "';"
        print(query)
        cur.execute(query)
        players = cur.fetchall()
        cur.close()
        conn.close()
        # print(players)
        
        return render_template('rankings.html', players=players)
    return render_template('rankings.html')


@app.route('/atp2019', methods=['GET','POST'])
def atp2019():
    if request.method == 'POST':
        player_name = request.form['playername']
        # surface = request.form['surface']
        # print(player_name,surface)
        
        conn = get_db_connection()
        cur = conn.cursor()
        query = "select winner_name, loser_name, surface, tourney_name, round, score, w_ace, w_df, l_ace, l_df from atp_matches_2019 where winner_name = '" + player_name + "' OR loser_name = '" + player_name + "';"
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        conn.close()
        print(results)
        return render_template('/atp2019.html', results = results)
    return render_template('/atp2019.html')

@app.route('/atp2020', methods=['GET','POST'])
def atp2020():
    if request.method == 'POST':
        player_name = request.form['playername']
        # surface = request.form['surface']
        
        
        conn = get_db_connection()
        cur = conn.cursor()
        query = "select winner_name, loser_name, surface, tourney_name, round, score, w_ace, w_df, l_ace, l_df from atp_matches_2020 where winner_name = '" + player_name + "' OR loser_name = '" + player_name + "';"
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        conn.close()
        print(results)
        return render_template('/atp2020.html', results = results)
    return render_template('/atp2020.html')

@app.route('/atp2021', methods=['GET','POST'])
def atp2021():
    if request.method == 'POST':
        player_name = request.form['playername']
        # surface = request.form['surface']
        
        
        conn = get_db_connection()
        cur = conn.cursor()
        query = "select winner_name, loser_name, surface, tourney_name, round, score, w_ace, w_df, l_ace, l_df from atp_matches_2021 where winner_name = '" + player_name + "' OR loser_name = '" + player_name + "';"
        cur.execute(query)
        results = cur.fetchall()
        cur.close()
        conn.close()
        print(results)
        return render_template('/atp2021.html', results = results)
    return render_template('/atp2021.html')


@app.route('/playeradmin2', methods = ['GET','POST'])
def playeradmin2():
    if request.method == 'POST':
        first_name = request.form['d_fname']
        last_name = request.form['d_lname']
        conn = get_db_connection()
        cur = conn.cursor()
        query = "delete from dummy_atp_players where name_first = '" +first_name+ "' and name_last = '" +last_name+ "';"
        cur.execute(query)
        conn.commit()
        return render_template('/success.html')
    return render_template('/playeradmin.html')



@app.route('/playeradmin', methods = ['GET', 'POST'])
def playeradmin():
    # populatetable()
    if request.method == 'POST':
        first_name = request.form['fname']
        last_name = request.form['lname']
        hand = request.form['gridRadios']
        ioc = request.form['ioc']
        wiki_id = request.form['wikid']
        height = request.form['height']     
        
        print(first_name,last_name,hand,ioc,wiki_id,height)
        conn = get_db_connection()
        cur = conn.cursor()
        if height == '' and wiki_id == '':
            query = "insert into dummy_atp_players values (nextval('players_sequence'),'" +first_name+ "','" +last_name+ "','" +hand+ "','" +ioc+ "');"
            cur.execute(query)
            conn.commit()
        # cur.execute(query)
        # print(query)
        return render_template('/success.html')
    conn = get_db_connection()
    cur = conn.cursor()
    query = "select * from dummy_atp_players"
    cur.execute(query)
    players = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('/playeradmin.html', players=players)


@app.route('/edit/<id>', methods=['POST','GET'])
def get_player_id(id):
    conn = get_db_connection()
    cur = conn.cursor()
    query = "SELECT * FROM dummy_atp_players where player_id = " +id+ ";"
    cur.execute(query)
    data = cur.fetchall()
    cur.close()
    print(data[0])
    return render_template('edit_player.html', player = data[0])

@app.route('/update/<id>', methods=['POST'])
def update_student(id):
    if request.method == 'POST':
        first_name = request.form['fname']
        last_name = request.form['lname']
        hand = request.form['hand']
        ioc = request.form['ioc']
        wiki_id = request.form['wikid']
        if wiki_id == "None":
            wiki_id = ""
        height = request.form['height']
        if height == "None":
            height = "" 
        conn = get_db_connection()
        cur = conn.cursor()
        # cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        if height == "" and wiki_id == "" :
            query = "UPDATE DUMMY_ATP_PLAYERS SET name_first = '" +first_name+ "', name_last = '" +last_name+ "', hand = '" +hand+ "', ioc = '" +ioc+ "' where player_id = " +id+ ";"
            cur.execute(query)
            conn.commit()
            return render_template('/playeradmin.html')
        else :
            query = "UPDATE DUMMY_ATP_PLAYERS SET name_first = '" +first_name+ "', name_last = '" +last_name+ "', hand = '" +hand+ "', ioc = '" +ioc+ "', height = " +height+ ", wikidata_id = '" +wiki_id+ "' where player_id = " +id+ ";"
            cur.execute(query)
        # flash('Student Updated Successfully')
            conn.commit()
        return render_template('/success.html')
    
@app.route('/delete/<id>', methods = ['POST','GET'])
def delete_student(id):
    conn = get_db_connection()
    cur = conn.cursor()
    query = "DELETE FROM dummy_atp_players where player_id = " +id+ ";"
    print(query)
    cur.execute(query)
    conn.commit()
    # flash('Student Removed Successfully')
    return render_template('/success.html')
 

if __name__ == "__main__":
    app.run(debug=True)