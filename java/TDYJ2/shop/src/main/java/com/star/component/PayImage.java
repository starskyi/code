package com.star.component;

import com.star.utils.ImageIoUtil;

import javax.swing.*;
import java.awt.*;
import java.awt.image.BufferedImage;
import java.io.IOException;

public class PayImage extends JPanel {
    BufferedImage image;

    public PayImage(){
        setPreferredSize(new Dimension(710, 970));
        try {
            this.image = ImageIoUtil.read("img/QR.jpg");
        } catch (IOException e) {
            e.printStackTrace();
        }

    }

    @Override
    public void paint(Graphics g) {
        g.drawImage(image, 0, 0, null);
    }
}
