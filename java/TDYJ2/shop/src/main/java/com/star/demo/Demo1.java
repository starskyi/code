package com.star.demo;


import com.star.domain.User;
import com.star.mapper.UserMapper;
import org.apache.ibatis.io.Resources;
import org.apache.ibatis.session.SqlSession;
import org.apache.ibatis.session.SqlSessionFactory;
import org.apache.ibatis.session.SqlSessionFactoryBuilder;

import javax.swing.*;
import java.awt.*;
import java.awt.event.MouseEvent;
import java.awt.event.MouseListener;
import java.io.IOException;
import java.io.InputStream;
import java.sql.Connection;
import java.util.List;


public class Demo1 {
    public static void main(String[] args){
        JFrame jf = new JFrame();

        JTextField input = new JTextField("请输入", 30);
        JButton btn = new JButton("搜索");

        JLabel l1 = new JLabel("登录");
        JLabel l2 = new JLabel("注册");

        JPanel p1 = new JPanel();
        JPanel p2 = new JPanel();
        p1.add(input);
        p1.add(btn);
        p2.add(l1);
        p2.add(l2);


        Box box1 = Box.createHorizontalBox();

        box1.add(p1);
        box1.add(p2);

        Box box3 = Box.createVerticalBox();
        box3.add(box1);

        JLabel l3 = new JLabel("1");
        JLabel l4 = new JLabel("2");
        JLabel l5 = new JLabel("3");
        JLabel l6 = new JLabel("4");
        JLabel l7 = new JLabel("5");
        l3.addMouseListener(new MouseListener() {
            public void mouseClicked(MouseEvent e) {
                System.out.println("hahah");
            }

            public void mousePressed(MouseEvent e) {

            }

            public void mouseReleased(MouseEvent e) {

            }

            public void mouseEntered(MouseEvent e) {
                System.out.println("11111");
            }

            public void mouseExited(MouseEvent e) {

            }
        });
//        JPanel p3 = new JPanel();
//        p3.add(l3);
//        p3.add(l4);
//        p3.add(l5);
//        p3.add(l6);
//        p3.add(l7);
        Box box2 = Box.createHorizontalBox();
        box2.add(l3);
        box2.add(l4);
        box2.add(l5);
        box2.add(l6);
        box2.add(l7);

        box1.setMaximumSize(new Dimension(800, 30));
        box2.setMaximumSize (new Dimension(800, 30));
        //box3.add(Box.createVerticalStrut(0));
        box3.add(box2);

        String resource = "mybatis-config.xml";
        try {
            InputStream inputStream = Resources.getResourceAsStream(resource);
            SqlSessionFactory sqlSessionFactory = new SqlSessionFactoryBuilder().build(inputStream);
            SqlSession sqlSession = sqlSessionFactory.openSession();
            UserMapper mapper = sqlSession.getMapper(UserMapper.class);
            List<User> all = mapper.findAll();
            System.out.println(all);
        } catch (IOException e) {
            e.printStackTrace();
        }
        jf.add(box3);
        //jf.pack();
        jf.setBounds(500, 500, 1000, 600);
        jf.setVisible(true);
    }
}
