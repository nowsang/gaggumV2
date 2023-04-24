const express = require('express');
const app = express();

app.get('/', function(req, res){
    res.send('hello NodeJs');
})
app.listen(8080, () => console.log('8080번 포트 대기'));