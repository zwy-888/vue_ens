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
                    更新:
                </h1>
                <form action="javascript:" method="post">
                    <table cellpadding="0" cellspacing="0" border="0"
                           class="form_table">
                        <tr>
                            <td valign="middle" align="right">
                                id:
                            </td>
                            <td valign="middle" align="left">
                                {{id}}
                            </td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">
                                姓名:
                            </td>
                            <td valign="middle" align="left">
                                <input type="text" class="inputgri" name="name" value="zhangshan" v-model="username"/>
                            </td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">
                                照片:
                            </td>
                            <td valign="middle" align="left">
                                <input type="file" name="photo" ref="photo"/>
                            </td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">
                                薪资:
                            </td>
                            <td valign="middle" align="left">
                                <input type="text" class="inputgri" name="salary" value="20000" v-model="salary"/>
                            </td>
                        </tr>
                        <tr>
                            <td valign="middle" align="right">
                                年龄:
                            </td>
                            <td valign="middle" align="left">
                                <input type="text" class="inputgri" name="age" value="20" v-model="age"/>
                            </td>
                        </tr>
                    </table>
                    <p>
                        <input type="submit" class="button" value="提交" @click="update"/>
                    </p>
                </form>
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
        name: "Udate",
        data() {
            return {
                id: '',
                user_obj: '',
                username: '',
                img: '',
                salary: '',
                age: '',
            }
        },

        methods: {
            find() {
                this.$axios.get("http://127.0.0.1:8000/api/emp/" + this.id + "/").then(response => {
                    console.log(response.data.results, '后台数据'),
                        console.log(this.id, '2222222222')
                        this.user_obj = response.data.results
                    this.username = this.user_obj.emp_name
                    this.age = this.user_obj.age
                    this.salary = this.user_obj.salary
                }).catch(error => {
                })
            },
            update() {
                let file = this.$refs.photo.files[0]
                // ajax请求上传文件借助于FormData, 方法是post  enctype是multipart/form-data
                let formData = new FormData();

                formData.append("emp_name", this.username);

                // formData.append("id", this.id);
                formData.append("salary", this.salary);
                formData.append("age", this.age);
                formData.append("img", this.$refs.photo.files[0])
                console.log(FormData);
                this.$axios({
                    url: "http://127.0.0.1:8000/api/emp/" + this.id + "/",
                    method: "patch",
                    data: formData,
                    headers: {
                        "content-type": "multipart/form-data"
                    },
                }).then(response => {
                    console.log(response.data);
                    if (response.data.message) {
                        this.$message({
                            message: '恭喜你，修改成功',
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
                // this.$axios({
                //     url:'http://127.0.0.1:8000/api/emp/',
                //     method:'patch',
                //     data(){
                //         username = this.username;
                //         age = this.age;
                //     }
                //
                // })
            },
        },

        created() {
            // 页面渲染前要获取路由id
            let url1 = this.$route.params.id
            console.log(url1);
            this.id = url1
            //也可把url放入find函数里
            this.find()
        }
    }
</script>

<style scoped>

</style>
