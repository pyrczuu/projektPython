from exercise_class import Exercise

#chest
bench_press = Exercise("Bench press", "chest", True)
incline_bench_press = Exercise("Incline Bench press", "chest", True)
chest_flys = Exercise("Chest flys", "chest", False)
push_up = Exercise("Push up", "chest", True)
chest_exercises = [bench_press,incline_bench_press,chest_flys,push_up]

#back
pull_up = Exercise("Pull up", "back", True)
lat_pulldown = Exercise("Lat pulldown", "back", False)
cable_row = Exercise("Cable row", "back", False)
barbell_row = Exercise("Barbell row", "back", True)
dumbbell_row = Exercise("Dumbbell row", "back", True)
chest_supported_row = Exercise("Chest supported row", "back", True)
face_pull = Exercise("Face pull", "back, shoulders", False)
pullover = Exercise("Pullover", "back", True)
back_exercises = [pull_up, lat_pulldown, cable_row, barbell_row, dumbbell_row, chest_supported_row, face_pull, pullover]

#biceps
barbell_curl = Exercise("Barbell curl", "biceps", True)
db_curl = Exercise("Dumbbell curl", "biceps", True)
hammer_curl = Exercise("Hammer curl", "biceps", True)
incline_curl = Exercise("Incline curl", "biceps", True)
reverse_grip_curl = Exercise("Reverse grip curl", "biceps", True)
preacher_curl = Exercise("Preacher curl", "biceps", True)
bicep_exercises = [barbell_curl, db_curl, hammer_curl, incline_curl, reverse_grip_curl, preacher_curl]

#triceps
triceps_pushdown = Exercise("Triceps pushdown", "triceps", False)
overhead_triceps_extension = Exercise("Overhead triceps extension", "triceps", False)
skullcrusher = Exercise("Skullcrusher", "triceps", True)
dips = Exercise("Dips", "triceps", True)
jm_press = Exercise("JM press", "triceps", True)
triceps_kickbacks = Exercise("Triceps kickbacks", "triceps", True)
triceps_exercises = [triceps_pushdown, overhead_triceps_extension,skullcrusher, dips, jm_press, triceps_kickbacks]

#shoulder exercises
lateral_raise = Exercise("Lateral raise", "shoulders", True)
overhead_press = Exercise("Overhead press", "shoulders", True)
reverse_db_fly = Exercise("Reverse dumbbell fly", "shoulders", True)
shoulder_exercises = [lateral_raise, overhead_press, reverse_db_fly, face_pull]

#legs
squats = Exercise("Squats", "legs", True)
leg_extensions = Exercise("Leg extensions", "legs", False)
bulgarian_split_squats = Exercise("Bulgarian split squats", "legs", True)
calve_raise = Exercise("Calve raise", "legs", True)
hip_thrust = Exercise("Hip thrust", "legs", False)
leg_press = Exercise("Leg press", "legs", False)
romanian_deadlift = Exercise("Romanian deadlift", "legs", True)
hamstring_curl = Exercise("Hamstring curl", "legs", False)
leg_exercises = [squats, leg_extensions, bulgarian_split_squats, calve_raise, hip_thrust, leg_press, romanian_deadlift, hamstring_curl]
