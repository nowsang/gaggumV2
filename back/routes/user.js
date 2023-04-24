var express = require("express");
var axios = require("axios");
const router = express.Router();
const KAKAO_OAUTH_TOKEN_API_URL = "https://kauth.kakao.com/oauth/token";
const KAKAO_GRANT_TYPE = "authorization_code";
const KAKAO_CLIENT_id = "58acce2e1c5607a9310ef74870273737";
// const KAKAO_REDIRECT_URL = "http://localhost:3000/auth/kakao/callback";
const KAKAO_REDIRECT_URL = "https://j8b310.p.ssafy.io/auth/kakao/callback";
const users = require("../servies/user");

router.get("/kakao/code", async function (req, res, next) {
  let code = req.query.code;
  try {
    axios
      .post(
        `${KAKAO_OAUTH_TOKEN_API_URL}?grant_type=${KAKAO_GRANT_TYPE}&client_id=${KAKAO_CLIENT_id}&redirect_uri=${KAKAO_REDIRECT_URL}&code=${code}`,
        {
          headers: {
            "Content-type": "application/x-www-form-urlencoded;charset=utf-8",
          },
        }
      )
      .then((result) => {
        console.log(result.data["access_token"]);
        console.log(result.data);
        const access_token = result.data.access_token;

        if (access_token) {
          console.log(`Bearer ${access_token}`);
          axios
            .post(
              "https://kapi.kakao.com/v2/user/me",
              {},
              {
                headers: {
                  Authorization: `Bearer ${access_token}`,
                  "Content-type": "apllication/x-www-form-urlencoded",
                },
              }
            )
            .then(async (result2) => {
              console.log("데이터성공 :");
              console.log(result2.data);
              const existUser = await users.getUserByEmail(result2.data);
              console.log("유저확인", existUser.data);
              if (existUser.data[0].vaild == 0) {
                console.log("회원가입 : ");
                users.signUpUser(result2.data);
              }
              const userData = await users.getUserByEmail2(result2.data);
              console.log("userData:", userData);
              res.json(userData);
            });
        }
      })
      .catch((e) => {
        console.log(e);
        res.send(e);
      });
  } catch (e) {
    console.log(e);
    res.send(e);
  }
});
router.post("/turtle", async function (req, res, next) {
  try {
    res.json(await users.updateUserTurtle(req.body));
  } catch (err) {
    console.error(`Error while getting turtle `, err.message);
    next(err);
  }
});

module.exports = router;
