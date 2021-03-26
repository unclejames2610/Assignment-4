import pymongo
import webbrowser

uri = "mongodb://ebuka:6iZMj8KC0VamKz8k1WBp4usu1XbRIIJiqSktBrm2MCvJCo4SmmAENsrdqT1Ubr1VIwWFI610cPPPyyN3nXnREg==@ebuka.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@ebuka@"
client = pymongo.MongoClient(uri)
client = pymongo.MongoClient()

db = client["OpenDefecation414"]
col = db["States"]
data = [{'state': 'Abia', 'value': 2.0},
        {'state': 'Adamawa', 'value': 19.4},
        {'state': 'Akwa Ibom', 'value': 4.3},
        {'state': 'Anambra', 'value': 6.9},
        {'state': 'Bauchi', 'value': 9.7},
        {'state': 'Bayelsa', 'value': 21.6},
        {'state': 'Benue', 'value': 45.9},
        {'state': 'Borno', 'value': 15.9},
        {'state': 'Cross River', 'value': 17.4},
        {'state': 'Delta', 'value': 25.9},
        {'state': 'Ebonyi', 'value': 58.3},
        {'state': 'Edo', 'value': 19.3},
        {'state': 'Ekiti', 'value': 44.6},
        {'state': 'Enugu', 'value': 40.4},
        {'state': 'Gombe', 'value': 7.6},
        {'state': 'Imo', 'value': 11.9},
        {'state': 'Jigawa', 'value': 14.0},
        {'state': 'Kaduna', 'value': 9.2},
        {'state': 'Kano', 'value': 4.3},
        {'state': 'Katsina', 'value': 8.2},
        {'state': 'Kebbi', 'value': 17.8},
        {'state': 'Kogi', 'value': 58.1},
        {'state': 'Kwara', 'value': 64.4},
        {'state': 'Lagos', 'value': 7.4},
        {'state': 'Nasarawa', 'value': 47.5},
        {'state': 'Niger', 'value': 47.8},
        {'state': 'Ogun', 'value': 17.7},
        {'state': 'Ondo', 'value': 34.7},
        {'state': 'Osun', 'value': 38.5},
        {'state': 'Oyo', 'value': 51.0},
        {'state': 'Plateau', 'value': 60.6},
        {'state': 'Rivers', 'value': 16.0},
        {'state': 'Sokoto', 'value': 18.1},
        {'state': 'Taraba', 'value': 41.3},
        {'state': 'Yobe', 'value': 32.4},
        {'state': 'Zamfara', 'value': 2.0},
        {'state': 'FCT', 'value': 37.0},
]
x = col.insert_many(data)


tbl = "<tr><td>State</td><td>Percentage</td></tr>"
data.append(tbl)

for y in col.find():
    a = "<tr><td>%s</td>" % y['state']
    data.append(a)
    b = "<td>%s</td></tr>" % y['value']
    data.append(b)

contents = '''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CEN 414 Project</title>
</head>
<body>
<h2>Below is a table showing the states in Nigeria with the percentage of people who still practice open defecation
</h2>
<form action = "formact.html" method = "post">
<label for= "states">Choose a state:</label>

<select name="states" id="states">
  <option value="Abia">Abia</option>
  <option value="Adamawa">Adamawa</option>
  <option value="Anambra">Anambra</option>
  <option value="Bauchi">Bauchi</option>
  <option value="Bayelsa">Bayelsa</option>
  <option value="Bauchi">Bauchi</option>
  <option value="Bayelsa">Bayelsa</option>
  <option value="Benue">Benue</option>
  <option value="Borno">Borno</option>
  <option value="Cross River">Cross River</option>
  <option value="Delta">Delta</option>
  <option value="Ebonyi">Ebonyi</option>
  <option value="Edo">Edo</option>
  <option value="Ekiti">Ekiti</option>
  <option value="Enugu">Enugu</option>
  <option value="Gombe">Gombe</option>
  <option value="Imo">Imo</option>
  <option value="Jigawa">Jigawa</option>
  <option value="Kaduna">Kaduna</option>
  <option value="Kano">Kano</option>
  <option value="Katsina">Katsina</option>
  <option value="Kebbi">Kebbi</option>
  <option value="Kogi">Kogi</option>
  <option value="Kwara">Kwara</option>
  <option value="Kwara">Kwara</option>
  <option value="Lagos">Lagos</option>
  <option value="Nasarawa">Nasarawa</option>
  <option value="Niger">Niger</option>
  <option value="Ogun">Ogun</option>
  <option value="Ondo">Ondo</option>
  <option value="Osun">Osun</option>
  <option value="Oyo">Oyo</option>
  <option value="Plateau">Plateau</option>
  <option value="Rivers">Rivers</option>
  <option value="Sokoto">Sokoto</option>
  <option value="Taraba">Taraba</option>
  <option value="Yobe">Yobe</option>
  <option value="Zamfara">Zamfara</option>
  <option value="FCT">FCT</option>
</select>
<br></br>
<input type = "submit" value = "Submit">
</form>

<table>
    %s
</table>
</body>
</html>
''' % data

filename = 'browser.html'


def main(contents, filename):
    output = open(filename, "w")
    output.write(contents)
    output.close()


main(contents, filename)
webbrowser.open(filename)
