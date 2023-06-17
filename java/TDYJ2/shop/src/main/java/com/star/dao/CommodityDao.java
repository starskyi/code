package com.star.dao;

import com.star.domain.Commodity;
import com.star.mapper.CommodityMapper;

import java.util.ArrayList;
import java.util.List;

import static com.star.ui.MainInterface.sqlSession;

public class CommodityDao {


    CommodityMapper mapper = sqlSession.getMapper(CommodityMapper.class);;

    /**
     * 查询所有商品
     * @return 所有商品
     */
    public List<Commodity> findAll(){

        List<Commodity> list = new ArrayList<Commodity>();
        list.addAll(mapper.selectByKind(8));
        list.addAll(mapper.findKindNotEight());
        return list;
    }

    /**
     * 根据id 查找商品
     * @param id 商品id
     * @return 返回商品
     */
    public Commodity selectById(int id){
        return mapper.selectById(id);
    }

    /**
     * 根据销量获取商品
     * @return 排序后的商品
     */
    public List<Commodity> selectByCount(){
        return mapper.selectByCount();
    }


    /**
     * 根据种类查询数据
     * @param kind 种类
     * @return 指定种类商品
     */
    public List<Commodity> selectByKind(int kind){
        return mapper.selectByKind(kind);
    }

    public List<Commodity> findKindNotEight(){
        return mapper.findKindNotEight();
    }

    public void del(String image){
        mapper.del(image);
    }

    public void add(Commodity commodity){
        mapper.add(commodity);
    }

    public void updateCount(int count, int id){
        mapper.updateCount(count, id);
    }

    public List<Commodity> selectByTitle(String title){
        return mapper.selectByTitle(title);
    }
}
