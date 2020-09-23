<template>
    <div id="wrap">
        <div id="top_content">
            <div id="header">
                <div id="rightheader">
                    <p>
                        2009/11/20
                        <br/>
                        <router-link to="/login">安全退出</router-link>
                        <router-link to="/index">返回主页</router-link>
                    </p>
                </div>
                <div id="topheader">
                    <h1 id="title">
                        <a href="#">Main</a>
                    </h1>
                </div>
                <div id="navigation">
                </div>
            </div>

            <div id="content">
                <p id="whereami">
                </p>
                <h1>
                    添加员工:
                </h1>
                <table cellpadding="0" cellspacing="0" border="0"
                       class="form_table">
                    <tr>
                        <td valign="middle" align="right">
                            name:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="name" v-model="emp_name"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            photo:
                        </td>
                        <td valign="middle" align="left">
                            <input type="file" name="photo" ref="photo"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            salary:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="salary" v-model="salary"/>
                        </td>
                    </tr>
                    <tr>
                        <td valign="middle" align="right">
                            age:
                        </td>
                        <td valign="middle" align="left">
                            <input type="text" class="inputgri" name="age" v-model="age"/>
                        </td>
                    </tr>
                </table>
                <p>
                    <input type="submit" class="button" value="确定添加" @click="add_emp"/>
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
        name: "Add",
        data() {
            return {
                emp_name: "",
                // photo: "",
                age: "",
                salary: "",
            }
        },
        methods: {
            // 添加员工的请求
            add_emp() {

                // 获取的页面的文件信息
                let file = this.$refs.photo.files[0]

                // ajax请求上传文件借助于FormData, 方法是post  enctype是multipart/form-data
                let formData = new FormData();
                formData.append("emp_name", this.emp_name);
                formData.append("salary", this.salary);
                formData.append("age", this.age);
                formData.append("img", this.$refs.photo.files[0])

                this.$axios({
                    url: "http://127.0.0.1:8000/api/emp/",
                    method: "post",
                    data: formData,
                    headers: {
                        "content-type": "multipart/form-data"
                    },
                }).then(response => {
                    console.log(response.data);
                    if (response.data.message) {

                        this.$message({
                            message: '恭喜你，添加成功',
                            type: 'success',
                            duration: 1000,
                            showClose: true,
                        })
                        // 跳转到列表页
                        this.$router.push("/index");
                    }
                }).catch(error => {
                    console.log(error.message);
                })
            },
        }
    }
</script>

<style scoped>

</style>
