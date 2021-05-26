#admin
from app import app
from app.models import *
from admin.forms import *
from app import db
import os
from flask import render_template,redirect,request,url_for,flash

### Admin panele giris hissesi

@app.route("/admin")
def index():
    return render_template("admin/index.html")


### Index.html about_section route

@app.route("/admin/about_s",methods=['POST','GET'])
def about_s():
    about_sections=About_section.query.all()
    if request.method=="POST":
        file=request.files['a_s_image']
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        about_section=About_section(
            a_s_title=request.form["a_s_title"],
            a_s_description=request.form["a_s_description"],
            a_s_link=request.form["a_s_link"],
            a_s_link_title=request.form["a_s_link_title"],
            a_s_image=filename
        )
        db.session.add(about_section)
        db.session.commit()
        return redirect(url_for('about_s'))
    return render_template("admin/about_section.html",about_sections=about_sections)


### Index.html Motivation_word route

@app.route("/motivation_word_section",methods=['POST','GET'])
def motivation_word_s():
    m_w_descriptions=Motivation_word_section.query.all()
    if request.method=="POST":
        m_w=Motivation_word_section(
            m_w_description=request.form["m_w_description"]
        )
        db.session.add(m_w)
        db.session.commit()
        return redirect(url_for('motivation_word_s'))
    return render_template("admin/motivation_word_section.html", m_w_descriptions= m_w_descriptions)


### Index.html Footer_Slider route

@app.route("/footer_slider",methods=['GET','POST'])  
def footer_slider_section():
    
    form=Footer_Slider_section_Form()
    Footer_S=Footer_Slider_section.query.all()
    if request.method=='POST':
        file=form.f_s_image.data
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        footer_slider=Footer_Slider_section(
            f_s_title=form.f_s_title.data,
            f_s_description=form.f_s_description.data,
            f_s_link=form.f_s_link.data,
            f_s_link_title=form.f_s_link_title.data,
            f_s_image=filename
        )
        db.session.add(footer_slider)
        db.session.commit()
        return redirect(url_for("footer_slider_section"))
    return render_template("admin/footer_slider_section.html",form=form,Footer_S=Footer_S)


### Index.html Slider route

@app.route("/slider",methods=['GET','POST'])  
def slider():
    form=Slider_section_Form()
    S=Slider_section.query.all()
    if request.method=='POST':
        file=form.s_image.data
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        slider=Slider_section(
            s_title=form.s_title.data,
            s_description=form.s_description.data,
            s_link=form.s_link.data,
            s_link_title=form.s_link_title.data,
            s_image=filename
        )
        db.session.add(slider)
        db.session.commit()
        return redirect(url_for("slider"))
    return render_template("admin/slider.html",form=form,S=S)



### Index.html Owners_of_the_page route  

@app.route("/Owners_of_the_page",methods=['GET','POST'])
def owners_of_the_page_section():
    form=Owners_of_the_page_section_Form()
    Owners=Owners_of_the_page_section.query.all()
    if request.method=='POST':
        file=form.own_image.data
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        owners_of_the_page=Owners_of_the_page_section(
            own_title=form.own_title.data,
            own_description=form.own_description.data,
            own_image=filename

        )
        db.session.add(owners_of_the_page)
        db.session.commit()
        return redirect(url_for("owners_of_the_page_section"))
    return render_template("admin/owners_of_the_page_section.html",form=form,Owners=Owners)


#Post Categories route

@app.route("/Post_Categories",methods=['GET','POST'])
def post_Categories():
    form=Post_Categories_Form()
    post_categories=Post_Categories.query.all()
    if request.method=='POST':
        file=form.s_image.data
        filename=file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'],filename))

        category=Post_Categories(
            p_c_title=form.p_c_title.data,
            p_c_description=form.p_c_description.data,
            p_c_link=form.p_c_link.data,
            p_c_link_title=form.p_c_link_title.data,
            p_c_image=filename
        )
        db.session.add(category)
        db.session.commit()
        return redirect(url_for("Post_Categories"))
    return render_template("admin/post_categories.html",form=form,post_categories=post_categories)








