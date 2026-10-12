import pybaseball as pb

def gather_pas(start, end):
    pitches = pb.statcast(start_dt=start, end_dt=end)
    pas = pitches[[
        "game_pk",
        "at_bat_number", 
        "game_date",
        "batter",
        "pitcher",
        "events",
        "description",
        "inning"
    ]]
    print(pas)

    return pas

# test = gather_pas("2025-03-27", "2025-09-28")
# test.to_csv("pas.csv")

# print(test.columns)



