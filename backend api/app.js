const express = require('express');
const cors = require('cors');
const bodyParser = require('body-parser');

const path = require('path')

const axios = require('axios');

const app = express();

// parse application/x-www-form-urlencoded
app.use(bodyParser.urlencoded({ extended: false }))
// parse application/json
app.use(bodyParser.json());

app.use(express.static(path.join(__dirname, 'public')))

app.use(cors())

const {
  userSheet, storyListSheet, userHistorySheet
} = require('./db/actions');

//故事列表
app.post('/story/getDataList', function (req, res, next) {
  storyListSheet.selectColum('*', (err, resdata) => {
    res.send({ status: 200, code: 'request success!', data: resdata });
  });
});

//故事详情
app.post('/story/detail/:id', function (req, res, next) {
  const sid = parseInt(req.params.id)
  storyListSheet.select({ sid }, (err, data) => {
    if (data.length > 0) {
      res.send({ status: 200, code: 'request success!', data: data[0] });
    } else {
      res.send({ status: 504, code: 'request error!' });
    }
  });
});

//历史列表
app.post('/history/getDataList', function (req, res, next) {
  let body = req.body;
  console.log(body)
  userHistorySheet.select(body, (err, resdata) => {
    res.send({ status: 200, code: 'request success!', data: resdata });
  });
});

//历史详情
app.post('/history/detail/:id', function (req, res, next) {
  const upid = parseInt(req.params.id)
  userHistorySheet.select({ upid }, (err, data) => {
    if (data.length > 0) {
      res.send({ status: 200, code: 'request success!', data: data[0] });
    } else {
      res.send({ status: 504, code: 'request error!' });
    }
  });
});


//用户新增记录
app.post('/story/addlog', function (req, res, next) {
  let body = req.body;
  userHistorySheet.insert(body, (err, data) => {
    if (err) {
      res.send({ status: 504, code: err });
      return;
    }
    if (data.affectedRows > 0) {
      res.send({ status: 200, code: 'request success!' });
    } else {
      res.send({ status: 503, code: 'request error!' });
    }
  });
});

//登录
app.post('/user/login', function (req, res, next) {
  let body = req.body;
  userSheet.select(body, (err, data) => {

    if (err) {
      res.send({ status: 504, code: 'db error!' });
      return;
    }
    if (data.length > 0) {
      let nowData = data[0];
      //密码匹配     
      if (nowData.password == body.password) {
        //密码不返回
        nowData.password = "";
        res.send({ status: 200, code: 'login success!' });
        return;
      }
    }
    res.send({ status: 504, code: 'password or account error!' });
  });
});



//端口为8111
const server = app.listen(8111, function () {
  console.log("登录地址:");
  console.log("http://localhost:" + server.address().port + "/login.html");
});