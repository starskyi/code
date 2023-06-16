package com.star.demo;

import com.star.component.CommodityPanel;
import com.star.domain.Commodity;

import javax.swing.*;
import java.awt.*;

public class Demo2 {
    public static void main(String[] args) {
        JFrame jf = new JFrame();

        JPanel p = new JPanel();

        //p.setPreferredSize(new Dimension(1000, 500));
        JScrollPane scrollPane = new JScrollPane(p);
//        crollPane.add(new CommodityPanel(new Commodity(1, "img/logo.jpg",
//                "小米10pro 最新研发， 超高性能，活动打折只要2999，包邮到家", 2999.0, 1000)));
//        //scrollPane.add(new JButton("哈哈"));

        for(int i = 0; i < 1000; i++){
            p.add(new JButton("13323"));

        }

        jf.add(scrollPane);

        jf.setBounds(500, 500, 1000, 800);
        jf.setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        jf.setVisible(true);
    }
}
