import random
last_names = [
    "Smith", "Johnson", "Williams", "Brown", "Jones", "Miller", "Davis", "Garcia", "Rodriguez", "Martinez", "Hernandez", "Lopez", "Gonzalez", "Wilson", "Anderson",
    "Thomas", "Taylor", "Moore", "Jackson", "Martin", "Lee", "Perez", "Thompson", "White", "Harris", "Sanchez", "Clark", "Ramirez", "Lewis", "Robinson", "Walker",
    "Young", "Allen", "King", "Wright", "Scott", "Torres", "Nguyen", "Hill", "Flores", "Green", "Adams", "Nelson", "Baker", "Hall", "Rivera", "Campbell", "Mitchell",
    "Carter", "Roberts", "Gomez", "Phillips", "Evans", "Turner", "Diaz", "Parker", "Cruz", "Edwards", "Collins", "Reyes", "Stewart", "Morris", "Morales", "Murphy",
    "Cook", "Rogers", "Gutierrez", "Ortiz", "Morgan", "Cooper", "Peterson", "Bailey", "Reed", "Kelly", "Howard", "Ramos", "Kim", "Cox", "Ward", "Richardson", "Watson",
    "Brooks", "Chavez", "Wood", "James", "Bennett", "Gray", "Mendoza", "Ruiz", "Hughes", "Price", "Alvarez", "Castillo", "Sanders", "Patel", "Myers", "Long", "Ross",
    "Foster", "Jimenez", "Powell", "Jenkins", "Perry", "Russell", "Sullivan", "Bell", "Coleman", "Butler", "Henderson", "Barnes", "Gonzales", "Fisher", "Vasquez",
    "Simmons", "Romero", "Jordan", "Patterson", "Alexander", "Hamilton", "Graham", "Reynolds", "Griffin", "Wallace", "Moreno", "West", "Cole", "Hayes", "Bryant",
    "Herrera", "Gibson", "Ellis", "Tran", "Medina", "Aguilar", "Stevens", "Murray", "Ford", "Castro", "Marshall", "Owens", "Harrison", "Fernandez", "McDonald",
    "Woods", "Washington", "Kennedy", "Wells", "Vargas", "Henry", "Chen", "Freeman", "Webb", "Tucker", "Guzman", "Burns", "Crawford", "Olson", "Simpson", "Porter",
    "Hunter", "Gordon", "Mendez", "Silva", "Shaw", "Snyder", "Mason", "Dixon", "Munoz", "Hunt", "Hicks", "Holmes", "Palmer", "Wagner", "Black", "Robertson", "Boyd",
    "Rose", "Stone", "Salazar", "Fox", "Warren", "Mills", "Meyer", "Rice", "Schmidt", "Garza", "Daniels", "Ferguson", "Nichols", "Stephens", "Soto", "Weaver", "Ryan",
    "Gardner", "Wright", "Beck", "Chapman", "Moore", "Ruiz", "Wong", "Evans", "Bishop", "Wheeler", "Lane", "Stanley", "Larson", "Hogan", "Day", "Bowman", "Medina",
    "Fowler", "Brewer", "Hoffman", "Carlson", "Silva", "Pearson", "Holland", "Douglas", "Fleming", "Jensen", "Vargas", "Byrd", "Davidson", "Hopkins", "May", "Terry",
    "Herrera", "Wade", "Soto", "Walters", "Curtis", "Neal", "Caldwell", "Lowe", "Jennings", "Barnett", "Graves", "Jimenez", "Horton", "Shelton", "Barrett", "Obrien",
    "Castro", "Sutton", "Gregory", "McKinney", "Lucas", "Miles", "Craig", "Rodriquez", "Chambers", "Holt", "Lambert", "Fletcher", "Watts", "Bates", "Hale", "Rhodes",
    "Pena", "Beck", "Newman", "Haynes", "McDaniel", "Mendez", "Bush", "Vaughn", "Parks", "Dawson", "Santiago", "Norris", "Hardy", "Love", "Steele", "Curry", "Powers",
    "Schultz", "Barker", "Guzman", "Page", "Munoz", "Ball", "Keller", "Chandler", "Weber", "Leonard", "Walsh", "Lyons", "Ramsey", "Wolfe", "Schneider", "Mullins",
    "Benson", "Sharp", "Bowen", "Daniel", "Barber", "Cummings", "Hines", "Baldwin", "Griffith", "Valdez", "Hubbard", "Salinas", "Reeves", "Warner", "Stevenson", "Burgess",
    "Santos", "Tate", "Cross", "Garner", "Mann", "Mack", "Moss", "Thornton", "Dennis", "McGee", "Farmer", "Delgado", "Aguilar", "Vega", "Glover", "Manning", "Cohen",
    "Harmon", "Rodgers", "Robbins", "Newton", "Todd", "Blair", "Higgins", "Ingram", "Reese", "Cannon", "Strickland", "Townsend", "Potter", "Goodwin", "Walton", "Rowe",
    "Hampton", "Ortega", "Patton", "Swanson", "Joseph", "Francis", "Goodman", "Maldonado", "Yates", "Becker", "Erickson", "Hodges", "Rios", "Conner", "Adkins", "Webster",
    "Norman", "Malone", "Hammond", "Flowers", "Cotton", "Kerr", "Crosby", "Berg", "Dougherty", "Forbes", "Burris", "Palmer", "Simon", "Shannon", "Townsend", "Dudley",
    "Nash", "Christian", "Phelps", "Farrell", "Castaneda", "Nash", "Dickerson", "Bond", "Wyatt", "Foley", "Chase", "Gates", "Vincent", "Mathews", "Hodge", "Garrison",
    "Trevino", "Villarreal", "Heath", "Dalton", "Valencia", "Callahan", "Hensley", "Atkins", "Huffman", "Roy", "Boyer", "Shields", "Lin", "Hancock", "Grimes", "Glenn",
    "Cline", "Delacruz", "Camacho", "Dillon", "Parrish", "Oneill", "Melton", "Booth", "Kane", "Berg", "Harrell", "Pitts", "Savage", "Wiggins", "Brennan", "Salas",
    "Marks", "Russo", "Sawyer", "Baxter", "Golden", "Hutchinson", "Liu", "Walter", "McDowell", "Wiley", "Rich", "Humphrey", "Johns", "Koch", "Suarez", "Hobbs", "Beard",
    "Gilmore", "Ibarra", "Keith", "Macias", "Khan", "Andrade", "Ware", "Stephenson", "Henson", "Wilkerson", "Dyer", "McClure", "Blackwell", "Mercado", "Tanner", "Eaton",
    "Clay", "Barron", "Beasley", "Oneal", "Preston", "Small", "Wu", "Zamora", "MacDonald", "Vance", "Snow", "McClain", "Stafford", "Orozco", "Barry", "English", "Shannon",
    "Kline", "Jacobson", "Woodard", "Huang", "Kemp", "Mosley", "Prince", "Merritt", "Hurst", "Villanueva", "Roach", "Nolan", "Lam", "Yoder", "McCormick", "Lerner", "Maddox",
    "Jarvis", "Barnett", "Shah", "Brown", "Novak", "Yung", "Han", "Valentine", "Hilton", "Wiley", "Rhodes", "Pence", "McLain", "Elmore", "Cervantes", "Lue", "Farias",
    "Gonzales", "Sosa", "Nicholson", "Monroe", "Wolf", "Morrow", "Kirk", "Randall", "Anthony", "Whitaker", "O'Connor", "Skinner", "Ware", "Molina", "Kirby", "Huffman",
    "Bradford", "Charles", "Gilmore", "Dominguez", "Oneal", "Bruce", "Lang", "Combs", "Kramer", "Heath", "Hancock", "Gallagher", "Gaines", "Shaffer", "Short", "Wiggins",
    "Mathews", "McClain", "Fischer", "Wall", "Small", "Melton", "Hensley", "Bond", "Dyer", "Cameron", "Grimes", "Contreras", "Christian", "Wyatt", "Baxter", "Snow", "Mosley",
    "Shepherd", "Larsen", "Hoover", "Beasley", "Glenn", "Petersen", "Whitehead", "Meyers", "Keith", "Garrison", "Vincent", "Shields", "Horn", "Savage", "Olsen", "Schroeder",
    "Hartman", "Woodard", "Mueller", "Kemp", "Deleon", "Booth", "Patel", "Calhoun", "Wiley", "Eaton", "Cline", "Navarro", "Harrell", "Lester", "Humphrey", "Parrish", "Duran",
    "Hutchinson", "Hess", "Dorsey", "Bullock", "Robles", "Beard", "Dalton", "Avila", "Vance", "Rich", "Blackwell", "York", "Johns", "Blankenship", "Trevino", "Salinas", "Campos",
    "Pruitt", "Moses", "Callahan", "Golden", "Montoya", "Hardin", "Guerra", "McDowell", "Carey", "Stafford", "Gallegos", "Henson", "Wilkinson", "Booker", "Merritt", "Miranda",
    "Atkinson", "Orr", "Decker", "Hobbs", "Preston", "Tanner", "Knox", "Pacheco", "Stephenson", "Glass", "Rojas", "Serrano", "Marks", "Hickman", "English", "Sweeney", "Strong",
    "Prince", "McClure", "Conway", "Walter", "Roth", "Maynard", "Farrell", "Lowery", "Hurst", "Nixon", "Weiss", "Trujillo", "Ellison", "Sloan", "Juarez", "Winters", "McLean",
    "Randolph", "Leon", "Boyer", "Villarreal", "McCall", "Gentry", "Carrillo", "Kent", "Ayers", "Lara", "Shannon", "Sexton", "Pace", "Hull", "Leblanc", "Browning", "Velasquez",
    "Leach", "Chang", "House", "Sellers", "Herring", "Noble", "Foley", "Bartlett", "Mercado", "Landry", "Durham", "Walls", "Barr", "McKee", "Bauer", "Rivers", "Everett", "Bradshaw",
    "Pugh", "Velez", "Rush", "Estes", "Dodson", "Morse", "Sheppard", "Weeks", "Camacho", "Bean", "Barron", "Livingston", "Middleton", "Spears", "Branch", "Blevins", "Chen", "Kerr",
    "McConnell", "Hatfield", "Harding", "Ashley", "Solis", "Herman", "Frost", "Giles", "Blackburn", "William", "Pennington", "Woodward", "Finley", "McIntosh", "Koch", "Best",
    "Solomon", "McCullough", "Dudley", "Nolan", "Blanchard", "Rivas", "Brennan", "Mejia", "Kane", "Benton", "Joyce", "Buckley", "Haley", "Valentine", "Maddox", "Russo", "McKnight",
    "Buck", "Moon", "McMillan", "Crosby", "Berg", "Dotson", "Mays", "Roach", "Church", "Chan", "Richmond", "Meadows", "Faulkner", "Oneill", "Knapp", "Kline", "Barry", "Ochoa",
    "Jacobson", "Gay", "Avery", "Hendricks", "Horne", "Shepard", "Hebert", "Cherry", "Cardenas", "McIntyre", "Whitney", "Waller", "Holman", "Donaldson", "Cantu", "Terrell", "Morin",
    "Gillespie", "Fuentes", "Tillman", "Sanford", "Bentley", "Peck", "Key", "Salas", "Rollins", "Gamble", "Dickson", "Battle", "Santana", "Cabrera", "Cervantes", "Howe", "Hinton",
    "Hurley", "Spence", "Zamora", "Yang", "McNeil", "Suarez", "Case", "Petty", "Gould", "McFarland", "Sampson", "Carver", "Bray", "Rosario", "Macdonald", "Stout", "Hester", "Melendez",
    "Dillon", "Farley", "Hopper", "Galloway", "Potts", "Bernard", "Joyner", "Stein", "Aguirre", "Osborn", "Mercer", "Bender", "Franco", "Rowland", "Sykes", "Benjamin", "Travis",
    "Pickett", "Crane", "Sears", "Mayo", "Dunlap", "Hayden", "Wilder", "McKay", "Coffey", "McCarty", "Ewing", "Cooley", "Vaughan", "Bonner", "Cotton", "Holder", "Stark", "Ferrell",
    "Cantrell", "Fulton", "Lynn", "Lott", "Calderon", "Rosa", "Pollard", "Hooper", "Burch", "Mullen", "Fry", "Riddle", "Levy", "David", "Duke", "Odonnell", "Guy", "Michael", "Britt",
    "Frederick", "Daugherty", "Berger", "Dillard", "Alston", "Jarvis", "Frye", "Riggs", "Chaney", "Odom", "Duffy", "Fitzpatrick", "Valenzuela", "Merrill", "Mayer", "Alford", "McPherson",
    "Acevedo", "Donovan", "Barrera", "Albert", "Cote", "Reilly", "Compton", "Raymond", "Mooney", "McGowan", "Craft", "Cleveland", "Clemons", "Wynn", "Nielsen", "Baird", "Stanton", "Snider",
    "Rosales", "Bright", "Witt", "Stuart", "Hays", "Holden", "Rutledge", "Kinney", "Clements", "Castaneda", "Slater", "Hahn", "Emerson", "Conrad", "Burks", "Delaney", "Pate", "Lancaster",
    "Sweet", "Justice", "Tyson", "Sharpe", "Whitfield", "Talley", "Macias", "Irwin", "Burris", "Ratliff", "McCray", "Madden", "Kaufman", "Beach", "Goff", "Cash", "Bolton", "McFadden",
    "Levine", "Good", "Byers", "Kirkland", "Kidd", "Workman", "Carney", "Dale", "Mcleod", "Holcomb", "England", "Finch", "Head", "Burt", "Hendrix", "Sosa", "Haney", "Franks", "Sargent",
    "Nieves", "Downs", "Rasmussen", "Bird", "Hewitt", "Lindsay", "Le", "Foreman", "Valencia", "Oneil", "Delacruz", "Vinson", "Dejesus", "Hyde", "Forbes", "Gilliam", "Guthrie", "Wooten",
    "Huber", "Barlow", "Boyle", "McMahon", "Buckner", "Rocha", "Puckett", "Langley", "Knowles", "Cooke", "Velazquez", "Whitley", "Noel", "Vang"
]


# You can now append these additional names to the previously generated list.
#middle_names.extend(additional_middle_names)
#middle_names_list = random.sample(middle_names,400)
# Firstnameslist = random.sample(middle, 400)
additional_names = [
    "Corbin", "Steele", "Huddleston", "Faulk", "Corbett", "Lockhart", "Mettler",
    "Pine", "Whitcomb", "Rafferty", "Stalder", "Tuggle", "Cromwell", "Dahl", "Whelan"
]
last_names.extend(additional_names)
with open('materials/Raw materials/Raw_Lastname.txt', 'w') as f:
    for name in last_names:
        f.write(name + '\n')
