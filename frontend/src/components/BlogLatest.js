import React from 'react'

function BlogLatest() {
    return (
        <>
          <section className="features-main my-2">
            <h2 className="md"><i className="fas fa-blog"></i>  dernier de notre blog </h2>
            <div className="grid">
                <div className="card flex" data-aos="slide-right">
                    <img src="images/eating.jpg" alt="" />
                    <p>
                        <span className="lead">Lorem ipsum dolor sit amet, consectetur tate velit esse</span>
                        <br />
                        <small>
                            Lorem ipsum dolor sit amet, consectetur tate velit esse
                            cillum dolore eu fugiat nulla pariatur.
                        </small>
                        
                        <br /> <br />
                        <small>date published: 25th Jan, 2020</small> <small>Time: 2weeks ago</small>
                    </p>
                    
                </div>

                <div className="card flex" data-aos="slide-left">
                    <img src="images/bg2.jpg" alt="" />
                    <p>
                        <span className="lead">Lorem ipsum dolor sit amet, consectetur tate velit esse</span>
                        <br />
                        <small>
                            Lorem ipsum dolor sit amet, consectetur tate velit esse
                            cillum dolore eu fugiat nulla pariatur.
                        </small>
                        
                        <br /> <br />
                        <small>date published: 25th Jan, 2020</small> <small>Time: 2weeks ago</small>
                    </p>
                </div>
            </div>
        </section>  
        </>
    )
}

export default BlogLatest;
