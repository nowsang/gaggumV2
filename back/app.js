const express = require('express');
const app = express();
const cors = require('cors');
const turtleRouter = require("./routes/turtle");
const diaryRouter = require("./routes/diary");
const plantRouter = require("./routes/plant");
const userRouter = require("./routes/user");
const socket  = require("./socket/socket");
app.use(cors());
app.use(express.json());

app.use('/plant',plantRouter);
app.use('/turtle',turtleRouter);
app.use('/diary',diaryRouter);
app.use('/user',userRouter);
app.get('/api', function(req, res){
    res.send('hello NodeJs');
})
app.listen(8080, () => console.log('8080번 포트 대기'));
socket.socketStart();