<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br/>
                    </p>
                </div>
                <div id="topheader">
                    <h1 id="title">
                        <a href="#">main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>
            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    login
                </h1>
                <table cellpadding="0" cellspacing="0" border="0"
                       class="form_table">
                    <tr>
                        <td valign="middle" align="right">
                            username:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="name" v-model="username"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            password:
                        </td>
                        <td valign="middle" align="left">
                            <input type="password" class="inputgri" name="pwd" v-model="password"/>
                        </td>
                    </tr>
                </table>
                <p>
                    <input type="submit" class="el-button" value="登录" @click="user_login"/>
                    &nbsp;&nbsp;
                    <!--                    <a href="">注册</a>-->
                    <router-link to="/register">注册</router-link>
                </p>
            </div>
        </div>
        <div id="footer">
            <div id="footer_bg">
                ABC@126.com
            </div>
        </div>
    </div>

</template>

<script>
    export default {
        name: "Login",
        data() {
            return {
                username: '',
                password: '',
            }
        },
        methods: {
            // 用户登录请求
            user_login() {
                this.$axios({
                    url: 'http://127.0.0.1:8000/api/login/',
                    method: 'post',
                    data: {
                        account: this.username,
                        pwd: this.password,
                    }
                }).then(response => {
                    // console.log(response.data);
                    // console.log(response.token);
                    console.log(response.data.token)
                    if (response.data.message) {
                        this.$message({
                            message: '恭喜你，登录成功',
                            duration: 1000,
                            showClose: true
                        })
                        // 将用户信息存入sessionstoreage 在主页的欢迎进行对用户的渲染
                        let username = response.data.results['username']
                        sessionStorage.setItem('user', username)
                        // console.log(response.data.token)
                        this.$router.push('/index')
                    } else {
                        this.$message.error('用户名或密码错误')
                    }
                }).catch(error => {
                    console.log(error)
                })
            }
        }
    }
</script>

<style scoped>

</style>
