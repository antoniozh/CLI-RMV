# Bash-RMV

### Bash-RMV is a fast, lightweight way to get your everyday RMV connection.

The idea behind this app is based on the frustration of spending to much time on the RMV website.

# Usage

Print the next connections from `Darmstadt Schloß` to `Darmstadt Hauptbahnhof`  
`./bash-RMV.py -O "Darmstadt Schloß" -D "Darmstadt Hauptbahnhof"`

Print the next connections from `Darmstadt Schloß` to `Darmstadt Hauptbahnhof` with `departure` at around `12:00`  
`./bash-RMV.py -O "Darmstadt Schloß" -D "Darmstadt Hauptbahnhof" -d 12:00`

Print the next connections from `Darmstadt Schloß` to `Darmstadt Hauptbahnhof`  with `arrival` at around `12:00`  
`./bash-RMV.py -O "Darmstadt Schloß" -D "Darmstadt Hauptbahnhof" -a 12:00`


# connections.ini

To **overcome redundancy** with your everyday connections you can save `connections` to a `ini` file

    [work]
    origin: Dieburg Hochschule Süd
    destination: Darmstadt Jugendstilbad

and use it on the terminal

`./bash-RMV.py -c work`

or  

`./bash-RMV.py -c work -d 14:00`



# Todo

* write `setup.py`


# Similar Apps
https://github.com/ysangkok/console-transit-trip-planner
