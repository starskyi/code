package com.star.demo;

import javax.swing.*;
import java.awt.*;

public class Demo3 {
    public static void main(String[] args) {
        JFrame jf = new JFrame();
        jf.setBounds(500, 500, 1800, 1000);

        JPanel p = new JPanel();
        JPanel jPanel = new JPanel();
        jPanel.setPreferredSize(new Dimension(1000, 8000));
        JScrollPane scrollPane = new JScrollPane(jPanel);

        for(int i = 0; i < 1000; i++){
            jPanel.add(new JButton("按钮" + i));
        }

        Box box = Box.createHorizontalBox();
        box.add(scrollPane);
//        p.add(scrollPane);
        jf.add(box);
        jf.setVisible(true);
    }
}
