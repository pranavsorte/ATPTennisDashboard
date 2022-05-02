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
        winner = request.form['winner']
        loser = request.form['loser']
        surface = request.form['surface']
        tournament = request.form['tourneyname']
        waces = request.form['waces']
        laces = request.form['laces']
        wdfs = request.form['wdfs']
        ldfs = request.form['ldfs']
        
        # print(player_name,surface)
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        query = "select winner_name, loser_name, surface, tourney_name, round, score, w_ace, w_df, l_ace, l_df from atp_matches_2019 where winner_name = '" + winner + "'"
        if loser != "":
            query = query + " AND loser_name = '" +loser+ "'"
        if surface != "":
            query = query + " AND surface = '" +surface+ "' "
        if tournament != "":
            query = query + " AND tourney_name = '" +tournament+ "' "
        if waces != "":
            query = query + " AND CAST(coalesce(w_ace,'0') AS INTEGER) >= " +waces+ ""
        if laces != "":
            query = query + " AND CAST(coalesce(l_ace,'0') AS INTEGER) >= " +laces+ ""
        if wdfs != "":
            query = query + " AND CAST(coalesce(w_df,'0') AS INTEGER) >= " +wdfs+ ""
        if ldfs != "":
            query = query + " AND CAST(coalesce(l_df,'0') AS INTEGER) >= " +ldfs+ ""
        
        print(query)
        
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
        winner = request.form['winner']
        loser = request.form['loser']
        surface = request.form['surface']
        tournament = request.form['tourneyname']
        waces = request.form['waces']
        laces = request.form['laces']
        wdfs = request.form['wdfs']
        ldfs = request.form['ldfs']
        
        # print(player_name,surface)
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        query = "select winner_name, loser_name, surface, tourney_name, round, score, w_ace, w_df, l_ace, l_df from atp_matches_2020 where winner_name = '" + winner + "'"
        if loser != "":
            query = query + " AND loser_name = '" +loser+ "'"
        if surface != "":
            query = query + " AND surface = '" +surface+ "' "
        if tournament != "":
            query = query + " AND tourney_name = '" +tournament+ "' "
        if waces != "":
            query = query + " AND CAST(coalesce(w_ace,'0') AS INTEGER) >= " +waces+ ""
        if laces != "":
            query = query + " AND CAST(coalesce(l_ace,'0') AS INTEGER) >= " +laces+ ""
        if wdfs != "":
            query = query + " AND CAST(coalesce(w_df,'0') AS INTEGER) >= " +wdfs+ ""
        if ldfs != "":
            query = query + " AND CAST(coalesce(l_df,'0') AS INTEGER) >= " +ldfs+ ""
        
        print(query)
        
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
        winner = request.form['winner']
        loser = request.form['loser']
        surface = request.form['surface']
        tournament = request.form['tourneyname']
        waces = request.form['waces']
        laces = request.form['laces']
        wdfs = request.form['wdfs']
        ldfs = request.form['ldfs']
        
        # print(player_name,surface)
        
        conn = get_db_connection()
        cur = conn.cursor()
        
        query = "select winner_name, loser_name, surface, tourney_name, round, score, w_ace, w_df, l_ace, l_df from atp_matches_2021 where winner_name = '" + winner + "'"
        if loser != "":
            query = query + " AND loser_name = '" +loser+ "'"
        if surface != "":
            query = query + " AND surface = '" +surface+ "' "
        if tournament != "":
            query = query + " AND tourney_name = '" +tournament+ "' "
        if waces != "":
            query = query + " AND CAST(coalesce(w_ace,'0') AS INTEGER) >= " +waces+ ""
        if laces != "":
            query = query + " AND CAST(coalesce(l_ace,'0') AS INTEGER) >= " +laces+ ""
        if wdfs != "":
            query = query + " AND CAST(coalesce(w_df,'0') AS INTEGER) >= " +wdfs+ ""
        if ldfs != "":
            query = query + " AND CAST(coalesce(l_df,'0') AS INTEGER) >= " +ldfs+ ""
        
        print(query)
        
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
        query = "delete from atp_players where name_first = '" +first_name+ "' and name_last = '" +last_name+ "';"
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
        # wiki_id = request.form['wikid']
        height = request.form['height']     
        
        print(first_name,last_name,hand,ioc,height)
        conn = get_db_connection()
        cur = conn.cursor()
        if height == '':
            query = "insert into atp_players values (nextval('players_sequence'),'" +first_name+ "','" +last_name+ "','" +hand+ "','" +ioc+ "');"
            cur.execute(query)
            conn.commit()
        else :
            query = "insert into atp_players values (nextval('players_sequence'),'" +first_name+ "','" +last_name+ "','" +hand+ "','" +ioc+ "'," +height+ ");"
            cur.execute(query)
            conn.commit()
            
        # cur.execute(query)
        # print(query)
        return render_template('/success.html')
    conn = get_db_connection()
    cur = conn.cursor()
    query = "select * from atp_players"
    cur.execute(query)
    players = cur.fetchall()
    cur.close()
    conn.close()
    return render_template('/playeradmin.html', players=players)


@app.route('/edit/<id>', methods=['POST','GET'])
def get_player_id(id):
    conn = get_db_connection()
    cur = conn.cursor()
    query = "SELECT * FROM atp_players where player_id = " +id+ ";"
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
            query = "UPDATE ATP_PLAYERS SET name_first = '" +first_name+ "', name_last = '" +last_name+ "', hand = '" +hand+ "', ioc = '" +ioc+ "' where player_id = " +id+ ";"
            cur.execute(query)
            conn.commit()
            return render_template('/playeradmin.html')
        else :
            query = "UPDATE ATP_PLAYERS SET name_first = '" +first_name+ "', name_last = '" +last_name+ "', hand = '" +hand+ "', ioc = '" +ioc+ "', height = " +height+ ", wikidata_id = '" +wiki_id+ "' where player_id = " +id+ ";"
            cur.execute(query)
        # flash('Student Updated Successfully')
            conn.commit()
        return render_template('/success.html')
    
@app.route('/delete/<id>', methods = ['POST','GET'])
def delete_student(id):
    conn = get_db_connection()
    cur = conn.cursor()
    query = "DELETE FROM atp_players where player_id = " +id+ ";"
    print(query)
    cur.execute(query)
    conn.commit()
    # flash('Student Removed Successfully')
    return render_template('/success.html')

@app.route('/insertmatch', methods = ["POST", "GET"])
def insertmatch():
    if request.method == 'POST':
        match_id = request.form['matchid']
        tname = request.form['tname']
        surface = request.form['surface']
        winner_id = request.form['winner_id']
        wname = request.form['wname']
        loserid = request.form['loserid']
        losername = request.form['losername']
        round = request.form['round']
        score = request.form['score']
        waces = request.form['waces']
        wdfs = request.form['wdfs']
        laces = request.form['laces']
        ldfs = request.form['ldfs']
        wrank = request.form['wrank']
        lrank = request.form['lrank']
        season = request.form['gridRadios']
        
        
        print(match_id,tname,surface,winner_id,wname,loserid,losername,round,score,waces,wdfs,laces,ldfs,wrank,lrank,season)
        conn = get_db_connection()
        cur = conn.cursor()

        if season == '2019':
            query = "INSERT INTO atp_matches_2019 VALUES (" +match_id+ ",'" +tname+ "','" +surface+ "'," +winner_id+ ",'" +wname+ "'," +loserid+ ",'" +losername+ "','" +round+ "','" +score+ "'," +waces+ "," +wdfs+ "," +laces+ "," +ldfs+ "," +wrank+ "," +lrank+ ");" 
            print(query)
            cur.execute(query)
            conn.commit()
            return render_template('/success.html')
        elif season == '2020':
            query = "INSERT INTO atp_matches_2020 VALUES (" +match_id+ ",'" +tname+ "','" +surface+ "'," +winner_id+ ",'" +wname+ "'," +loserid+ ",'" +losername+ "','" +round+ "','" +score+ "'," +waces+ "," +wdfs+ "," +laces+ "," +ldfs+ "," +wrank+ "," +lrank+ ");" 
            print(query)
            cur.execute(query)
            conn.commit()
            return render_template('/success.html')
        else :
            query = "INSERT INTO atp_matches_2021 VALUES (" +match_id+ ",'" +tname+ "','" +surface+ "'," +winner_id+ ",'" +wname+ "'," +loserid+ ",'" +losername+ "','" +round+ "','" +score+ "'," +waces+ "," +wdfs+ "," +laces+ "," +ldfs+ "," +wrank+ "," +lrank+ ");" 
            print(query)
            cur.execute(query)
            conn.commit()
            return render_template('/success.html')
        
        
        # return render_template('/success.html')
    return render_template('/insertmatch.html')

@app.route('/edit_matches/<id>/<season>', methods=["POST","GET"])
def get_match_id(id,season):
    # if request.method == 'POST':
    # print(season)
    # print(id)
    # season = request.form['gridRadios']
    # print(season)
    conn = get_db_connection()
    cur = conn.cursor()
    if season == '2019':
        query = "SELECT * FROM atp_matches_2019 where match_id = " +id+ ";"
        cur.execute(query)
        data = cur.fetchall()
        cur.close()
        print(data[0])
        return render_template('edit_match.html', player = data[0], season=season)
    elif season == '2020':
        query = "SELECT * FROM atp_matches_2020 where match_id = " +id+ ";"
        cur.execute(query)
        data = cur.fetchall()
        cur.close()
        print(data[0])
        return render_template('edit_match.html', player = data[0], season=season)
    else :
        query = "SELECT * FROM atp_matches_2021 where match_id = " +id+ ";"
        cur.execute(query)
        data = cur.fetchall()
        cur.close()
        print(data[0])
        return render_template('edit_match.html', player = data[0], season=season)

    print("")
        
        
        
    
    
    # return render_template('/edit_match.html')
    
    
 
@app.route('/updatematches', methods=["POST","GET"])
def updatematches():
    if request.method == 'POST':
        conn = get_db_connection()
        cur = conn.cursor()
        
        season = request.form['seasonselect']
        print(season)
        if season == "2019":
            query = "select * from atp_matches_2019"
            cur.execute(query)
            players = cur.fetchall()
            cur.close()
            conn.close()
            return render_template('/updatematches.html',players=players, season = '2019')
        
        elif season == "2020":
            query = "select * from atp_matches_2020"
            cur.execute(query)
            players = cur.fetchall()
            cur.close()
            conn.close()
            return render_template('/updatematches.html',players=players, season='2020')
        
        else :
            query = "select * from atp_matches_2021"
            cur.execute(query)
            players = cur.fetchall()
            cur.close()
            conn.close()
            return render_template('/updatematches.html',players=players, season='2021')
            
    return render_template('/updatematches.html')


@app.route('/update_match/<id>/<season>', methods=['POST'])
def update_match(id,season):
    if request.method == 'POST':
        score = request.form['score']
        waces = request.form['waces']
        wdfs = request.form['wdfs']
        laces = request.form['laces']
        ldfs = request.form['ldfs']
        
        if season == '2019':
            conn = get_db_connection()
            cur = conn.cursor()
            query = "update atp_matches_2019 set score = '" +score+ "', w_ace = " +waces+ ", w_df= " +wdfs+ ", l_ace = " +laces+ ", l_df = " +ldfs+ " where match_id = " +id+ ";"
            cur.execute(query)
            conn.commit()
            return render_template('/success.html')
        elif season == '2020':
            conn = get_db_connection()
            cur = conn.cursor()
            query = "update atp_matches_2020 set score = '" +score+ "', w_ace = " +waces+ ", w_df= " +wdfs+ ", l_ace = " +laces+ ", l_df = " +ldfs+ " where match_id = " +id+ ";"
            cur.execute(query)
            conn.commit()
            return render_template('/success.html')
        else :
            conn = get_db_connection()
            cur = conn.cursor()
            query = "update atp_matches_2021 set score = '" +score+ "', w_ace = " +waces+ ", w_df= " +wdfs+ ", l_ace = " +laces+ ", l_df = " +ldfs+ " where match_id = " +id+ ";"
            cur.execute(query)
            conn.commit()
            return render_template('/success.html')
        

@app.route('/delete_matches/<id>/<season>', methods = ['POST','GET'])
def delete_match(id,season):
    conn = get_db_connection()
    cur = conn.cursor()
    if season == '2019':
        query = "DELETE from atp_matches_2019 where match_id = " +id+ ";"
        cur.execute(query)
        conn.commit()
        return render_template('/success.html')
    elif season == '2020':
        query = "DELETE from atp_matches_2020 where match_id = " +id+ ";"
        cur.execute(query)
        conn.commit()
        return render_template('/success.html')
    else:
        query = "DELETE from atp_matches_2021 where match_id = " +id+ ";"
        cur.execute(query)
        conn.commit()
        return render_template('/success.html')
            
            
        

if __name__ == "__main__":
    app.run(debug=True)