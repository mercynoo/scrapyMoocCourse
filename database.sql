create database scrapy DEFAULT CHARACTER SET utf8 COLLATE utf8_general_ci;
use scrapy;
CREATE TABLE moocCourse (
    title VARCHAR(100) NOT NULL PRIMARY KEY , # 课程标题
    url VARCHAR(150), # 课程的url
    image_url VARCHAR(150), # 课程图片
    introduction VARCHAR(150), # 课程描述
    student INTEGER(100), # 学生人数
    image_path VARCHAR(150) # 课程图片路径
)
