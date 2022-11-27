 # -*- coding: utf-8 -*-
"""This module contains all the author routes."""
from flasgger import swag_from
from flask import Blueprint, request, jsonify
from .controller import (
    handle_search_all_articles
)

search = Blueprint("search", __name__)


@search.route("/search", methods=["POST"])
@swag_from(
    "./docs/search.yml", endpoint="search.search_own_articles", methods=["POST"]
)
def search_own_articles():
    """Register an author."""
    # return handle_search_own_articles(request.args.get("id"), request.json)
    return jsonify({'success': 'serach all articles'})

@search.route("/search_all_articles", methods=["POST"])
@swag_from(
    "./docs/search_all_articles.yml", endpoint="search.search_all_articles", methods=["POST"]
)
def search_all_articles():
    """Register an author."""
    return handle_search_all_articles(request.args.get("author id"), request.json)


@search.route("/search_articles_read", methods=["POST"])
@swag_from(
    "./docs/search_articles_read.yml", endpoint="search.search_articles_read", methods=["POST"]
)
def search_articles_read():
    """Search articles read."""
    # return handle_search_articles_read(request.args.get("id"), request.json)
    return jsonify({'success': 'search articles read'})


@search.route("/search_articles_bookmarked", methods=["POST"])
@swag_from(
    "./docs/search_articles_bookmarked.yml", endpoint="search.search_articles_bookmarked", methods=["POST"]
)
def search_articles_bookmarked():
    """Search articles bookmarekd."""
    # return handle_search_articles_bookmarked(request.args.get("id"), request.json)
    return jsonify({'success': 'search articles bookmarked'})


@search.route("/search_articles_author_follows", methods=["POST"])
@swag_from(
    "./docs/search_articles_author_follows.yml", endpoint="search.search_articles_author_follows", methods=["POST"]
)
def search_articles_author_follows():
    """Search articles written by authors you follow."""
    # return handle_search_articles_author_follows(request.args.get("id"), request.json)
    return jsonify({'success': 'search articles bookmarked'})


@search.route("/search_articles_author_followers", methods=["POST"])
@swag_from(
    "./docs/search_articles_author_followers.yml", endpoint="search.search_articles_author_followers", methods=["POST"]
)
def search_articles_author_followers():
    """Search articles written by your followers."""
    # return handle_search_articles_author_followers(request.args.get("id"), request.json)
    return jsonify({'success': 'search articles bookmarked'})


@search.route("/search_articles_with_tags", methods=["POST"])
@swag_from(
    "./docs/search_articles_with_tags.yml", endpoint="search.search_articles_with_tags", methods=["POST"]
)
def search_articles_with_tags():
    """Search articles written by your followers."""
    # return handle_search_articles_with_tags(request.args.get("id"), request.json)
    return jsonify({'success': 'search articles bookmarked'})


@search.route("/search_articles_liked", methods=["POST"])
@swag_from(
    "./docs/search_articles_liked.yml", endpoint="search.search_articles_liked", methods=["POST"]
)
def search_articles_liked():
    """Search articles bookmarekd."""
    # return handle_search_articles_liked(request.args.get("id"), request.json)
    return jsonify({'success': 'search articles bookmarked'})


@search.route("/search_articles_commented", methods=["POST"])
@swag_from(
    "./docs/search_articles_commented.yml", endpoint="search.search_articles_commented", methods=["POST"]
)
def search_articles_commented():
    """Search articles bookmarekd."""
    # return handle_search_articles_commented(request.args.get("id"), request.json)
    return jsonify({'success': 'search articles bookmarked'})