<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br/>
<!--                        <router-link to="/login">安全退出</router-link>-->
                        <a  @click="zhuxiao">安全退出</a>
<!--                        <input type="submit" class="el-button" value="安全退出" @click="zhuxiao"/>-->

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
                    Welcome! {{user_msg}}
                </h1>
                <table class="table">
                    <tr class="table_header">
                        <td>
                            ID
                        </td>
                        <td>
                            Name
                        </td>
                        <td>
                            Photo
                        </td>
                        <td>
                            Salary
                        </td>
                        <td>
                            Age
                        </td>
                        <td>
                            Operation
                        </td>
                    </tr>
                    <tr class="row1" v-for="(emp,index) in user_list" :key="emp.id">
                        <td>
                            {{emp.id}}
                        </td>
                        <td>
                            {{emp.emp_name}}
                        </td>
                        <td>
                            <img :src=" emp.img" style="height: 60px;">
                            <!--                            // 绑定src属性不再取值-->

                        </td>
                        <td>
                            {{emp.salary}}
                        </td>
                        <td>
                            {{emp.age}}
                        </td>
                        <td>
                            <a href="javascript:" @click="del_emp(emp.id)">删除</a>
                            <!--                            <a href="javascript:" @click="updata_emp(emp.id)">更新</a>-->
                            <router-link :to="'/update/'+emp.id">更新</router-link>
                        </td>
                    </tr>
                </table>
                <p>
                    <!--                    <input type="button" class="button" value="Add Employee"/>-->
                    <el-button>
                        <router-link to="/add">添加员工</router-link>
                    </el-button>
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
        name: "Index",
        data() {
            return {
                user_msg: '',
                user_list: []
            }
        },
        methods: {
            // 加载页面数据之前渲染此页面数据，在钩子里执行此函数
            findall() {
                this.$axios.get('http://127.0.0.1:8000/api/emp/').then(response => {
                    console.log(response.data.results)
                    this.user_list = response.data.results
                }).catch(error => {
                })
            },

            // 删除员工
            del_emp(id) {
                if (confirm('确认要删除此员工吗？')) {
                    this.$axios({
                        url: "http://127.0.0.1:8000/api/emp/" + id + "/",
                        method: 'delete',
                    }).then(response => {
                        if (response.data.message) {
                            this.$message({
                                message: '删除成功',
                                type: 'success',
                                duration: 1000,
                            });
                            // 此处查询所有数据进行刷新数据
                            this.findall()
                        }
                    }).catch(error => {
                        this.$message.error('删除失败');
                    })
                }
            },
            zhuxiao() {
                // localStorage.removeItem('user')
                sessionStorage.clear()
                console.log(sessionStorage.getItem('user'))
                this.$message.error('注销成功')
                this.$router.push('/login');

            },
        },
        // 生命周期钩子在页面渲染完成前,
        created() {
            // this.zhuxiao()
            let username = sessionStorage.getItem('user')
            if (username) {
                this.user_msg = username
            } else {
                this.$message.error('对不起请到登录页面登录')
                this.$router.push('/login');
            }
            // 此处查询所有数据进行刷新数据

            this.findall()
        }
    }
</script>

<style scoped>

</style>
