# Bash-RMV

### Bash-RMV is a fast, lightweight way to get your everyday RMV connection.

The idea behind this app is based on the frustration of spending to much time on the RMV website.

# Usage

Print the next connections from `Darmstadt Schloß` to `Darmstadt Hauptbahnhof`  
`./bash_RMV.py -O "Darmstadt Schloß" -D "Darmstadt Hauptbahnhof"`

Print the next connections from `Darmstadt Schloß` to `Darmstadt Hauptbahnhof` with `departure` at around `12:00`  
`./bash_RMV.py -O "Darmstadt Schloß" -D "Darmstadt Hauptbahnhof" -d 12:00`

Print the next connections from `Darmstadt Schloß` to `Darmstadt Hauptbahnhof`  with `arrival` at around `12:00`  
`./bash_RMV.py -O "Darmstadt Schloß" -D "Darmstadt Hauptbahnhof" -a 12:00`


# connections.ini

To **overcome redundancy** with your everyday connections you can save `connections` to a `ini` file

    [work]
    origin: Dieburg Hochschule Süd
    destination: Darmstadt Jugendstilbad

and use it on the terminal

`./bash_RMV.py -c work`

or  

`./bash_RMV.py -c work -d 14:00`

# outcome

`./bash_RMV.py -c work -d 14:00` would produce the following outcome.


    ------------------------------------------------

    from:	Dieburg Hochschule Süd
    to:	  Darmstadt Jugendstilbad


    dep.:	13:50
    arr.:	14:42
    dur.:	0:52


    trans.:	Bus K 68, RB 75, Tram 6, Bus K 55

    ------------------------------------------------

    from:	Dieburg Hochschule Süd
    to:	  Darmstadt Jugendstilbad


    dep.:	14:19
    arr.:	14:43
    dur.:	0:24


    trans.:	Bus 671

    ------------------------------------------------

    from:	Dieburg Hochschule Süd
    to:	  Darmstadt Jugendstilbad


    dep.:	14:49
    arr.:	15:13
    dur.:	0:24


    trans.:	Bus 671

    ------------------------------------------------




# Todo

* write `setup.py`


# Similar Apps
https://github.com/ysangkok/console-transit-trip-planner
