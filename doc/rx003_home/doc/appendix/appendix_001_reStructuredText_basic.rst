.. _restructuredtext_basic:


reStructuredText 기초문법
****************************************************************

* 다음 웹페이지들을 참조했음
    * `<https://sublime-and-sphinx-guide.readthedocs.io/en/latest>`_
    * `<https://www.sphinx-doc.org/en/master>`_


Sections
===========================================================

* parts (Sprint)

    .. code-block:: RST

        Parts title
        #####################################################################

* chapters (Day)

    .. code-block:: RST

        Chapter title
        ****************************************************************

* sections (Work)

    .. code-block:: RST

        Section title
        ===========================================================

* subsections

    .. code-block:: RST

        Subsection title
        ------------------------------------------------------

* subsubsections

    .. code-block:: RST

        Subsubsection title
        ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

* paragraphs

    .. code-block:: RST

        Paragraph title
        """"""""""""""""""""""""""""""""""""""""""""

* 구분 선
    .. code-block:: RST

        -------------------------------------------------------------------------------


Figures
===========================================================

.. code-block:: RST

    :numref:`figure_005_01_temp` 은 유비노스 구조를 보여준다.

    .. _figure_005_01_temp:

    .. figure:: /_static/image/ubinos_architecture.png
        :width: 90%
        :align: center
        :alt: Ubinos architecture

        Ubinos architecture


:numref:`figure_005_01_temp` 은 유비노스 구조를 보여준다.

.. _figure_005_01_temp:

.. figure:: /_static/image/ubinos_architecture.png
    :width: 90%
    :align: center
    :alt: Ubinos architecture

    Ubinos architecture


Equations
===========================================================

.. code-block:: RST

    로봇 회전각속도 :math:`w_k` 는 식 :eq:`eq1_temp` 을 사용해 구할수 있다.

    .. math::
        :label: eq1_temp

        v_k = \frac{\Delta s_k}{\Delta t} = \frac{v_k^r + v_k^l}{2} = \frac{r \left( \omega_k^r + \omega_k^l \right)}{2}


로봇 회전각속도 :math:`w_k` 는 식 :eq:`eq1_temp` 을 사용해 구할수 있다.

.. math::
    :label: eq1_temp

    v_k = \frac{\Delta s_k}{\Delta t} = \frac{v_k^r + v_k^l}{2} = \frac{r \left( \omega_k^r + \omega_k^l \right)}{2}


Table
===========================================================


.. code-block:: RST

    :numref:`table_91_temp` 은 ...

    .. _table_91_temp:

    .. table:: 표 예
        :align: center

        +------------------------+------------+----------+----------+
        | Header row, column 1   | Header 2   | Header 3 | Header 4 |
        | (header rows optional) |            |          |          |
        +========================+============+==========+==========+
        | body row 1, column 1   | column 2   | column 3 | column 4 |
        +------------------------+------------+----------+----------+
        | body row 2             | Cells may span columns.          |
        +------------------------+------------+---------------------+
        | body row 3             | Cells may  | - Table cells       |
        +------------------------+ span rows. | - contain           |
        | body row 4             |            | - body elements.    |
        +------------------------+------------+---------------------+


:numref:`table_91_temp` 은 ...

.. _table_91_temp:

.. table:: 표 예
    :align: center

    +------------------------+------------+----------+----------+
    | Header row, column 1   | Header 2   | Header 3 | Header 4 |
    | (header rows optional) |            |          |          |
    +========================+============+==========+==========+
    | body row 1, column 1   | column 2   | column 3 | column 4 |
    +------------------------+------------+----------+----------+
    | body row 2             | Cells may span columns.          |
    +------------------------+------------+---------------------+
    | body row 3             | Cells may  | - Table cells       |
    +------------------------+ span rows. | - contain           |
    | body row 4             |            | - body elements.    |
    +------------------------+------------+---------------------+


Hyperlinks
===========================================================


External links
------------------------------------------------------


.. code-block:: RST

    `Ubinos <https://ubinos.org>`_

    `<https://ubinos.org>`_


`Ubinos <https://ubinos.org>`_

`<https://ubinos.org>`_


Internal links
------------------------------------------------------


.. code-block:: RST

    :ref:`restructuredtext_basic`


:ref:`restructuredtext_basic`


기타 참고 사항
===========================================================

* 파일과 디렉토리 이름에 한글 포함시키면 안 된다.
    * 한글이 포함되면 latex pdf build 중에 오류가 발생할 수 있다.

