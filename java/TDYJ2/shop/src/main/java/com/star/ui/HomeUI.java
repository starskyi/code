package com.star.ui;

import com.star.component.CommodityPanel;
import com.star.component.GoodsPanel;
import com.star.domain.Commodity;

import javax.swing.*;
import java.awt.*;
import java.util.List;

public class HomeUI extends Box {

    public HomeUI(List<Commodity> goods) {
        super(BoxLayout.X_AXIS);

        JPanel panel = new JPanel();

        JScrollPane scrollPane = new JScrollPane(panel, JScrollPane.VERTICAL_SCROLLBAR_ALWAYS,
                JScrollPane.HORIZONTAL_SCROLLBAR_ALWAYS);
        scrollPane.setPreferredSize(new Dimension(1000, 2000));


        panel.setPreferredSize(new Dimension(2200, (goods.size()/3 + 1) * 320));
        for(Commodity commodity : goods){
            panel.add(new CommodityPanel(commodity));
        }

        add(scrollPane);

    }
}
