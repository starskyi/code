package com.star.dao.impl;

import com.star.dao.BookDao;

public class BookDaoImpl implements BookDao{

    public void save() {
        System.out.println("dao....");
    }

    public void init(){
        System.out.println("init");
    }

    public void destroy(){
        System.out.println("destroy");
    }

}