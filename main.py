import intercept
import kindle


def main():
    articles = intercept.get_articles()
    intercept.create_files(articles)
    kindle.convert_files()
    kindle.set_author()
    kindle.send_files()


if __name__ == "__main__":
    main()
