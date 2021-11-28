
/**** Table of registered users
 * 		Username, First name, Last name, and Password
 * 		PK = Username
 *  ****/
CREATE TABLE regUser (
	username		varchar(20), 
	firstname		varchar(100) NOT NULL,
	lastname		varchar(100) NOT NULL,
	password		varchar(20) NOT NULL,
	PRIMARY KEY	(username)
);


/**** Table of categories of incidents
 * 		Category ID and Category
 * 		PK = Category ID
 *  ****/
CREATE TABLE category (
	category_id		varchar(10),
	category		varchar(100) NOT NULL,
	PRIMARY KEY	(category_id)
);


/**** Table of incidents
 * 		Incident ID, Category ID, Description, Date created, Date resolved, 
 * 		State, Point of contact, and Current Assignee
 * 		PK = Incident ID
 * 		FK from Category ID to Category table
 * 		FK from Point of contact and Current Assignee to Registered Users table
 *  ****/
CREATE TABLE incident (
	incident_id			varchar(10),
	category_id			varchar(10),
	description			varchar(4000),
	date_created			date NOT NULL,
	date_resolved			date,
	state				varchar(7) NOT NULL,
	point_of_contact		varchar(20) NOT NULL,
	current_assignee		varchar(20) NOT NULL,
	PRIMARY KEY 	(incident_id),
	FOREIGN KEY	(category_id) REFERENCES category(category_id),
	FOREIGN KEY 	(point_of_contact) REFERENCES regUser(username),
	FOREIGN KEY 	(current_assignee) REFERENCES regUser(username),
	CHECK (state in ('open', 'closed', 'stalled'))
);


/**** Table of tags
 * 		Tag ID, Incident ID, Tag
 * 		PK = Tag ID
 * 		FK from Incident ID to Incident table
 *  ****/
CREATE TABLE tags (
	tag_id			varchar(10),
	incident_id		varchar(10) NOT NULL,
	tag 			varchar(100) NOT NULL,
	PRIMARY KEY 	(tag_id),
	FOREIGN KEY 	(incident_id) REFERENCES incident(incident_id)
);


/**** Table of case history
 * 		Update ID, Incident ID, Comment, Time of Update, Handler
 * 		PK = Update ID
 * 		FK from Incident ID to Incident table
 * 		FK from handlet to Registered Users table
 *  ****/
CREATE TABLE caseHistory (
	update_id 		varchar(10),
	incident_id		varchar(10) NOT NULL,
	comment			varchar(100) NOT NULL,
	time_of_update		timestamp NOT NULL,
	handler			varchar(20),
	PRIMARY KEY 	(update_id),
	FOREIGN KEY 	(incident_id) REFERENCES incident(incident_id),
	FOREIGN KEY 	(handler) REFERENCES regUser(username)
);

/********** UNSURE IF WE NEED ALL THESE INDEXES BECAUSE I KNOW THEY CAN ADD OVERHEAD *********/

/**** Primary Key Indexes ****/
CREATE INDEX pk_regUser_index ON regUser (username ASC);
CREATE INDEX pk_category_index ON category (category_id ASC);
CREATE INDEX pk_incident_index ON incident (incident_id ASC);
CREATE INDEX pk_tag_index ON tags (tag_id ASC);
CREATE INDEX pk_caseHistory_index ON caseHistory (update_id ASC);

/**** Foreign Key Indexes ****/
CREATE INDEX fk_incident_category_index ON incident (category_id ASC);
CREATE INDEX fk_incident_point_of_contact_index ON incident (point_of_contact ASC);
CREATE INDEX fk_incident_current_assignee_index ON incident (current_assignee ASC);
CREATE INDEX fk_tags_incident_id_index ON tags (incident_id ASC);
CREATE INDEX fk_caseHistory_incident_id_index ON caseHistory (incident_id ASC);
CREATE INDEX fk_caseHistory_handler_index ON caseHistory (handler ASC);

/**** Other Various Indexes ****/
CREATE INDEX regUser_lastname_index ON regUser (lastname ASC);
CREATE INDEX incident_date_created_index ON incident (date_created DESC);
CREATE INDEX caseHistory_time_of_update_index ON caseHistory (time_of_update DESC);

/**** View for all Incident Information
 * Incident ID, Date created, Date resolved, State, Category, Description, Point of contact, 
 * Current assignee, Tags, Time of update, Update comments, Update handler
 *  ****/
CREATE VIEW total_incident_view
AS 
	SELECT incident.incident_id, incident.date_created, incident.date_resolved, incident.state, 
	category.category, incident.description, incident.point_of_contact, incident.current_assignee, 
	tags.tag, caseHistory.time_of_update, caseHistory.comment, caseHistory.handler AS update_handler
	FROM incident
		LEFT JOIN category ON (incident.category_id = category.category_id)
		LEFT JOIN tags ON (incident.incident_id = tags.incident_id)
		LEFT JOIN caseHistory ON (incident.incident_id = caseHistory.incident_id)
		ORDER BY date_created DESC, time_of_update DESC;
