package com.star.mapper;

import com.star.domain.Commodity;
import com.star.domain.User;
import org.apache.ibatis.annotations.Select;

import java.util.List;

public interface CommodityMapper {

    @Select("select * from tb_commodity")
    List<Commodity> findAll();

    @Select("select * from tb_commodity where id = #{id}")
    Commodity selectById(int id);


    List<Commodity> selectByCount();

    @Select("select * from tb_commodity where kind = #{kind}")
    List<Commodity> selectByKind(int kind);

    @Select("select * from tb_commodity where kind != 8")
    List<Commodity> findKindNotEight();
}
