const express = require('express');
const req = require('express/lib/request');
const res = require('express/lib/response');

const {PythonShell} = require('python-shell');
const port = 8000;

const app = express();
app.use( express. urlencoded({ extended: true }))

// parse application/json
app.use(express.json()); 

app.get("/", () =>{
  res.end("Hello world ")
})

app.post('/main', callPython);

function callPython(req, res) {

    var options = {
      pythonPath: 'C:/Users/Addy/AppData/Local/Programs/Python/Python310/python3.exe',
      args:
        [
          "sadish", // replace with name,
          "placement_name",
          "effective_from",
          "effective_to",
          "a.csv",
          0
        ]
      }
      PythonShell.run('./backend/main.py', options, function (err, data) {
        if (err) res.send(err);
        res.send(data)
        console.log(req.body)

      });

}

app.listen(8000, () => console.log("App launching in port : 8000!"))


// req.body.name,
//           req.body.paramaters,
//           req.body.placement_name,
//           req.body.effective_from,
//           req.body.effective_to,
            //  req.body.upload_file,
            // req.body.active,