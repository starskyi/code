package com.star.utils;

import com.star.ui.MainInterface;

import javax.imageio.ImageIO;
import java.awt.image.BufferedImage;
import java.io.IOException;

public class ImageIoUtil {
    public static BufferedImage read(String filename) throws IOException {
        return ImageIO.read((MainInterface.class.getClassLoader().getResourceAsStream(filename)));
    }
}
