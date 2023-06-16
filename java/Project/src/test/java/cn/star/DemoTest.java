package cn.star;

import org.junit.Test;
import org.junit.Assert;

public class DemoTest{
	@Test
	public void sayTest(){
		String text = new Demo().say("maven");
		Assert.assertEquals("hello maven", text);
	}
}