package com.star.dao;

import com.star.domain.Record;
import com.star.domain.User;
import com.star.mapper.UserMapper;
import java.util.List;

import static com.star.ui.MainInterface.sqlSession;
import static com.star.ui.MainInterface.user;

public class UserDao {
    UserMapper mapper = sqlSession.getMapper(UserMapper.class);;


    /**
     * 查找所有用户
     * @return 所有用户
     */
    public List<User> findAll(){
        return mapper.findAll();
    }

    /**
     * 根据id 查找用户
     * @param id 用户编号
     * @return User
     */
    public User selectById(int id){
        return mapper.selectById(id);
    }

    /**
     * 添加用户
     * @param user 用户
     * @return 返回添加用户id
     */
    public boolean add(User user){
        int id = mapper.add(user);
        return id > 0;
    }

    /**
     * 完成商品购买
     * @param record 当前购买记录
     */
    public boolean buy(Record record){
        try{
            Double money = user.getMoney() - record.getPrice();

            user.setMoney(money);
            user.setId(mapper.update(user));

            record.setStatus(2);
            new RecordDao().updateStatus(record);

            return true;
        }catch (Exception e){
            e.printStackTrace();
        }

        return false;
    }

    public List<User> findClient(){
        return mapper.selectByStatus(0);
    }

    public List<User> findMerchant(){
        return mapper.selectByStatus(1);
    }

    public void delUser(String username){
        mapper.delByUsername(username);
    }
}
