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
                    注册
                </h1>
                <table cellpadding="0" cellspacing="0" border="0"
                       class="form_table">
                    <tr>
                        <td valign="middle" align="right">
                            用户名:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="username" v-model="username"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            真实姓名:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="name" v-model="real_name"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            密码:
                        </td>
                        <td valign="middle" align="left">
                            <input type="password" class="inputgri" name="pwd" v-model="password"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            确人密码:
                        </td>
                        <td valign="middle" align="left">
                            <input type="password" class="inputgri" name="pwd" v-model="re_pwd"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right" v-model="gender">
                            性别:
                        </td>
                        <td valign="middle" align="left">
                            男
                            <input type="radio" class="inputgri" name="sex" @click="gender=0" value="m"
                                   checked="checked"/>
                            女
                            <input type="radio" class="inputgri" name="sex" @click="gender=1" value="f"/>
                        </td>
                    </tr>

                </table>
                <p>
                    <input type="submit" class="el-button" value="注册 " @click="register"/>
                    <router-link to="/login">登录</router-link>

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
        name: "Register",
        data() {
            return {
                username: "",
                real_name: "",
                password: "",
                gender: 0,
                re_pwd: ""
            }
        },
        methods: {
            register() {
                // alert()
                //    发起访问请求
                this.$axios({
                    url: "http://127.0.0.1:8000/api/register/",
                    method: "post",
                    data: {
                        username: this.username,
                        real_name: this.real_name,
                        password: this.password,
                        gender: this.gender,
                        re_pwd: this.re_pwd,
                    },
                    // 下面放回成功或后台返回的值和失败返回的值
                }).then(response => {
                    console.log(response)
                    if (response.data.message) {
                        this.$message({
                            message: '恭喜你，注册成功',
                            duration: 1000,
                            showClose: true
                        })
                        //跳转页面
                        this.$router.push('/login')
                    }
                }).catch(error => {
                    console.log(error.message);
                    this.$message.error('用户名已存在或密码不一致')
                })
            },
        }
    }
</script>

<style scoped>

</style>
